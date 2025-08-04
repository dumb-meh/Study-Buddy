import os
import json
import openai
from dotenv import load_dotenv
from .story_schema import story_response

load_dotenv ()

class Story:
    def __init__(self):
        self.client=openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def create_story(self, input_data:str)->story_response:
        prompt=self.create_prompt()
        data=input_data
        response=self.get_openai_response (prompt,data)
        return response
    
    def create_prompt(self) -> str:
        return f"""You are a creative storyteller specializing in ADHD-friendly narratives. Your job is to transform any input text into an engaging, vivid story that captures and holds attention.

                **YOUR MISSION:**
                Create a captivating story based on the user's input text. Make it visual, exciting, and easy to follow for ADHD minds.

                **STORY REQUIREMENTS:**
                - **Length**: 200-400 words (long enough to be engaging, short enough to maintain focus)
                - **Structure**: Clear beginning, middle, and end
                - **Pacing**: Quick-moving with frequent action or dialogue
                - **Characters**: Relatable and distinctive (give them memorable traits)
                - **Setting**: Vivid and interesting locations
                - **Conflict**: Include tension, mystery, or adventure to maintain engagement

                **ADHD-FRIENDLY ELEMENTS:**
                - Use short paragraphs (2-3 sentences max)
                - Include sensory details (what characters see, hear, feel, smell)
                - Add dialogue to break up narrative
                - Create unexpected twists or surprises
                - Use active voice and strong verbs
                - Include humor when appropriate
                - Make it visual and cinematic

                **OUTPUT FORMAT:**
                You MUST respond with valid JSON in this exact structure:

                ```json
                {{
                "image_prompt": "A detailed DALL-E 3 prompt describing the main scene of the story. Include: setting, main characters, mood, art style (like 'digital art', 'illustration', 'fantasy art'), lighting, and key visual elements. Make it vivid and specific.",
                "title": "An engaging story title",
                "story": "The complete story text with proper paragraph breaks using \\n\\n for new paragraphs"
                }}
                ```

                **IMAGE PROMPT GUIDELINES:**
                - Describe the most visually striking scene from your story
                - Include character descriptions, setting details, mood/atmosphere
                - Specify an art style (digital art, illustration, fantasy art, etc.)
                - Keep it under 400 characters for DALL-E 3
                - Make it family-friendly and appropriate
                - Focus on the main action or central moment

                **STORY TRANSFORMATION RULES:**
                - If input is a single word/concept: Build an adventure around it
                - If input is a sentence: Expand it into a full narrative
                - If input is abstract: Make it concrete with characters and action
                - If input is factual: Turn it into an exciting story while keeping core truth

                **Remember**: ADHD brains love novelty, excitement, and visual storytelling. Make it impossible to look away!"""
    
    def get_openai_response (self, prompt:str, data:str)->str:
        completion =self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"system", "content": prompt},{"role":"user", "content": data}],
            temperature=0.7            
        )
        raw_content = completion.choices[0].message.content.strip()
        json_start = raw_content.find('{')
        json_text = raw_content[json_start:]

        if json_text.count('{') > json_text.count('}'):
            json_text += '}'
        
        try:
            parsed = json.loads(json_text)
            image_prompt = parsed["image_prompt"]
            story = {k: v for k, v in parsed.items() if k != "image_prompt"}
        
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON from LLM: {e}\n---\n{raw_content}")
        
        image_url = self.ai_generate_image(image_prompt)
        return story_response(story, image_url=image_url)
    
    def ai_generate_image(image_prompt: str) -> str:
        response = self.client.images.generate(
            model="dall-e-3", 
            prompt=image_prompt,
            n=1,
            size="1024x1024",
            quality="standard", 
            style="natural" 
        )


