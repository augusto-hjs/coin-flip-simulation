# coin-flip-simulation

A small Streamlit web application written in Python that simulates random coin flips and visualizes how the running mean converges toward 0.5 as the number of trials increases.

This project was developed during a Data Analyst Bootcamp, as part of the Software Development Tools module, within the Web Applications section. The focus was on building a simple web app, structuring a Python project, and deploying it using modern development workflows.

Live Demo  
https://coin-flip-simulation-9qre.onrender.com

Features  
- Interactive slider to choose the number of coin tosses  
- Real-time line chart showing the running mean of outcomes  
- Experiment history table stored using Streamlit session state  
- Simple and responsive UI built with Streamlit  

Tech Stack  
- Python  
- Streamlit  
- Pandas  
- SciPy  

How It Works  
The app simulates a fair coin flip using a Bernoulli random variable with probability p = 0.5. After each trial, the running mean of outcomes is updated and plotted, demonstrating the Law of Large Numbers as the mean converges toward 0.5 with more trials.

Run Locally  
Clone the repository, install the dependencies listed in requirements.txt, and run the application using the command: streamlit run app.py. The app will open automatically in your browser.

Project Context  
This project was created as part of a Bootcamp sprint focused on Software Development Tools, specifically the Web Applications module. The goal was to practice basic web app development in Python, interactive UI creation with Streamlit, dependency management, and cloud deployment using Render.

Deployment  
The application is deployed on Render using the free plan and is publicly accessible via the link above.

License  
This project is intended for educational and portfolio purposes.
