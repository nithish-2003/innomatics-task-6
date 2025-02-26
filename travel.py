# Import necessary libraries
import streamlit as st
from dotenv import load_dotenv
import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms.base import LLM
from pydantic import BaseModel, Field
from typing import List, Optional
import google.generativeai as genai

# Load environment variables securely
load_dotenv()

# Configure Google Generative AI with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Custom wrapper to integrate Google Generative AI with LangChain
class TravelAIModel(LLM, BaseModel):
    model_name: str = Field(..., description="Name of the AI model to use")  # Required field

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        print(f"Using model_name: {self.model_name}")  # Debug statement
        model = genai.GenerativeModel(self.model_name)
        
        response = model.generate_content(prompt)
        
        # Ensure correct extraction of the generated response
        if hasattr(response, "text") and response.text:
            return response.text.strip()
        elif hasattr(response, "candidates") and response.candidates:
            return response.candidates[0].content.strip()  # Corrected attribute access
        else:
            return "No valid response received from the AI model."

    @property
    def _llm_type(self) -> str:
        return "google_generative_ai"

# Define the template for generating travel suggestions
travel_prompt_template = PromptTemplate(
    input_variables=["source", "destination"],
    template="Find the best ways to travel from {source} to {destination}, including options like cab, train, bus, and flights. Include estimated costs and travel times."
)

# Function to generate travel suggestions using LangChain and Google Generative AI
def get_travel_suggestions(start_location: str, end_location: str) -> str:
    try:
        ai_model = TravelAIModel(model_name="gemini-1.5-flash")  # Ensure model_name is passed
        suggestion_chain = LLMChain(llm=ai_model, prompt=travel_prompt_template)
        suggestions = suggestion_chain.run(source=start_location, destination=end_location)
        return suggestions
    except Exception as e:
        return f"Error in AI model processing: {str(e)}"

# Main function to run the app
def main():
    st.title("AI-Powered Travel Planner")
    st.write("Plan your trip easily with AI-powered suggestions!")

    start_location = st.text_input("Where are you starting from?", placeholder="e.g., New York")
    end_location = st.text_input("Where do you want to go?", placeholder="e.g., India")

    if st.button("Show Travel Options"):
        if start_location and end_location:
            st.write(f"Finding travel options from {start_location} to {end_location}...")
            try:
                result = get_travel_suggestions(start_location, end_location)
                st.subheader("Here are your travel options:")
                st.write(result)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.error("Please enter both the starting location and the destination.")

# Run the app
if __name__ == "__main__":
    main()
