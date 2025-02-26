🌍 AI-Powered Travel Planner

🚀 Overview

The AI-Powered Travel Planner is a cutting-edge web application that helps users find the best travel options between locations. It leverages Google Generative AI and LangChain to generate detailed travel suggestions, including flights, trains, buses, and other modes of transportation.

✨ Features

🔍 AI-powered travel recommendations

🌐 Uses Google Generative AI (Gemini 1.5 Flash) for travel planning

📊 Estimates costs and travel times for multiple transport modes

🎛️ Interactive and user-friendly interface built with Streamlit

🔐 Secure API key management using dotenv

🛠️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-username/AI-Travel-Planner.git
cd AI-Travel-Planner

2️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate     # On Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Create a .env file in the root directory and add your Google API Key:

GOOGLE_API_KEY=your_google_api_key_here

5️⃣ Run the Application

streamlit run travel.py

🏗️ Project Structure

AI-Travel-Planner/
│-- travel.py                # Main application logic
│-- requirements.txt         # Python dependencies
│-- .env                     # API keys (not shared in GitHub)
│-- README.md                # Documentation
│-- assets/                  # Images & resources

⚡ How It Works

1️⃣ User Input: The app asks for starting location and destination.
2️⃣ AI Processing: The system uses LangChain + Google AI to generate travel options.
3️⃣ Results Displayed: The user sees the best travel routes, estimated costs, and travel time.

🔧 Tech Stack

Python 🐍

Streamlit 🎨 (Frontend)

Google Generative AI 🤖

LangChain 🔗 (AI Model Integration)

dotenv 🔐 (Secure API Management)

🎯 Future Enhancements

🛫 Real-time flight price tracking

🏨 Hotel & accommodation recommendations

🗺️ Route visualization with maps

🤖 Voice & Chatbot integration

🤝 Contributing

We welcome contributions! 🚀 Feel free to submit pull requests or open issues.

📜 License

MIT License. Free to use and modify! ✨

🌟 Show Your Support!

Give this project a ⭐ on GitHub if you found it helpful!

📬 Need Help?

Feel free to reach out via GitHub Issues!

