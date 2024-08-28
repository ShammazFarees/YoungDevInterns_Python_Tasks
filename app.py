# Importing Streamlit
import streamlit as st

# Setting the title of the page
st.set_page_config(page_title="Shammas's Resume", layout="wide")

# Using CSS in Python to make styles
st.markdown("""
    <style>
        
        @keyframes typing {
            from { width: 0; }
            to { width: 75%; }
        }

        @keyframes blink {
            0% { border-right: 2px solid transparent; }
            50% { border-right: 2px solid black; }
            100% { border-right: 2px solid transparent; }
        }

        .typing-animation {
            font-family: Sans-Serif;
            white-space: nowrap; /* Prevent text wrapping */
            overflow: hidden; /* Hide overflow */
            border-right: 2px solid black; /* Cursor effect */
            animation: typing 4s steps(30, end), blink 0.75s step-end infinite;
            font-size: 4em; /* Adjust size as needed */
            color: black; /* Change color as needed */
        }

        .profile-section {
            text-align: justify; /* Justifying the text */
            font-size: 16px;
            color: #333;
            margin-bottom: 20px;
        }

        .Employment-Section{
            text-align: justify;
        }

        .Education-Section{
            text-align: justify;
        }
        
    </style>
""", unsafe_allow_html=True)

#Header name 
st. sidebar.image("me.jpg", use_column_width=True)
st.markdown("""
    <div class="typing-animation">
        SHAMMAS FARIS
    </div>
""", unsafe_allow_html=True)

#subheader
st.subheader("Aspiring ML Engineer | Data Scientist")

# Define the CSS and HTML for the sidebar content
st.sidebar.markdown("""
    <style>
        .sidebar-content {
            display: flex;
            align-items: center;
            margin-bottom: 10px; /* Adjust as needed */
            background-color: ash;
        }
        .sidebar-image {
            margin-right: 5px; /* Adjust as needed */ 
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); /* Add shadow */
            background-color: black
        }    
    </style>
  <body>                 
    <div class="sidebar-content">
        <img src="https://w7.pngwing.com/pngs/243/358/png-transparent-black-and-white-e-mail-logo-email-computer-icons-icon-design-email-miscellaneous-angle-triangle.png" class="sidebar-image" width="50" />
        <span><b>Email:</b><br><a href=mailto:"shammazfarees@gmail.com"><em>shammazfarees@gmail.com</em></a></span>
    </div>
                    
    <div class="sidebar-content">
        <img src="https://th.bing.com/th/id/OIP.rCYX2GaTFqHfWdxR5HsVBQHaHa?rs=1&pid=ImgDetMain" class="sidebar-image" width="50" />
        <span><b>Phone:</b><br><em>+923158011848</em></span>
    </div>
                    
    <div class="sidebar-content">
        <img src="https://th.bing.com/th/id/R.cba56c5092e61caf6bfc85f6d986116b?rik=o3s7hWP16a0QEQ&pid=ImgRaw&r=0" class="sidebar-image" width="50" />
        <span><b>Address:</b><br><em>UCMD Boys Hostel, Block D Naz Town, Lahore, Punjab, 54600, Pakistan</em></span>
    </div>
                    
    <div class="sidebar-content">
        <img src="https://th.bing.com/th/id/OIP.fIaurFWI7I-kbLk9yGKSAwHaHa?rs=1&pid=ImgDetMain" class="sidebar-image" width="50" />
        <span><b>Nationality:</b><br><em>Sri Lankan</em></span>
    </div>
    <div class="sidebar-content">
        <img src="https://th.bing.com/th/id/OIP.Rnp0fWfpP4zyIz1F3b4zkwHaHa?rs=1&pid=ImgDetMain" class="sidebar-image" width="50" />
        <span><b>Linkedin:</b><br><a href="https://www.linkedin.com/in/shammas-faris" target="_blank"><em>https://www.linkedin.com/in/shammas-faris</em></a></span>
    </div>
    <div class="sidebar-content">
        <img src="https://th.bing.com/th/id/OIP.lJEV8azOsH7rRQJ6gmvt9gHaHa?rs=1&pid=ImgDetMain" class="sidebar-image" width="50" />
        <span><b>Github:</b><br><a href="https://github.com/ShammazFarees" target="_blank"><em>https://github.com/ShammazFarees</em></a></span>
    </div>
  </body>
""", unsafe_allow_html=True)

#Certificates section
st.sidebar.header("Certificates")
st.sidebar.markdown("""
    <style>
        .header-with-image {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }
                    
        .header-with-image img {
            width: 40px; /* Adjust size as needed */
            height: 40px; /* Adjust size as needed */
            margin-right: 10px; /* Space between image and text */
        }
                    
        .header-with-image h2 {
            margin: 0;
            font-size: 40px;
        } 
    </style>
                    
    <div class="certificates">
    <li><b>National Statistics Olympiad</b>-IASSL</li>
    <li><b>Python Developer</b>-Sololearn</li>
    <li><b>AI Prompting</b>-Sololearn</li>
    <li><b>OOP in Java</b>-Coursera</li>
    <li><b>Prompt Engineering</b>-Sololearn</li>
    <li><b>SQL</b>-Sololearn</li>
    <li><b>Responsible AI</b>-Google Cloud</li>
    <li><b>Introduction to Machine Learning</b>-Sololearn</li>
    <li><b>Machine Learning</b>-Simplilearn</li>
    <li><b>Data Analytics with AI</b>-Sololearn</li>
    <li><b>NumPy</b>-Wildlearner</li>
    <li><b>Git</b>-Wildlearner</li>
    </div><br>
""", unsafe_allow_html=True
)

#Skills Section
st.sidebar.header("Skills")
st.sidebar.markdown("""
    <div class="skills">
    <li>Leadership Qualities</li>
    <li>Attention to Detail</li>
    <li>Teamwork</li>
    <li>Presentation & Communication Skills</li>
    <li>Strong Knowledge in Math</li>
    <li>Statisics</li>
    <li>Problem Solving</li>
    </div><br>
""", unsafe_allow_html=True
)

#Languages Section
st.sidebar.header("Languages")
st.sidebar.markdown("""
    <style>
    .languages {
        margin-bottom: 20px;
    }

    .languages h4 {
        margin: 0;
        font-size: 16px;
        font-weight: normal;
        color: #333;
    }

    .progress-bar {
        width: 100%;
        background-color: #e0e0e0;
        border-radius: 25px;
        overflow: hidden;
        margin-top: 5px;
    }

    .progress {
        height: 8px;
        background-color: #3498db;
        border-radius: 25px;
    }
    </style>                
    <div class="languages">
        <h4>English</h4>
        <div class="progress-bar">
        <div class="progress" style="width: 90%;"></div>
      </div>
    </div>

    <div class="languages">
        <h4>Sinhala</h4>
        <div class="progress-bar">
        <div class="progress" style="width: 100%;"></div>
      </div>
    </div>

    <div class="languages">
        <h4>Tamil</h4>
        <div class="progress-bar">
        <div class="progress" style="width: 100%;"></div>
      </div>
    </div>
    
    <div class="languages">
        <h4>Urdu</h4>
        <div class="progress-bar">
        <div class="progress" style="width: 50%;"></div>
      </div>
    </div>
""", unsafe_allow_html=True)

#programmong Languages Section
st.sidebar.header("Programming Languages")
st.sidebar.markdown("""
    <style>
                    
    .skill {
        margin-bottom: 20px;
    }

    .skill h4 {
        margin: 0;
        font-size: 16px;
        font-weight: normal;
        color: #333;
    }

    .progress-bar {
        width: 100%;
        background-color: #e0e0e0;
        border-radius: 25px;
        overflow: hidden;
        margin-top: 5px;
    }

    .progress {
        height: 8px;
        background-color: #3498db;
        border-radius: 25px;
    }
                    
    </style>    
                                
    <div class="skill">
        <h4>Python</h4>
        <div class="progress-bar">
        <div class="progress" style="width: 70%;"></div>
      </div>
    </div>

    <div class="skill">
        <h4>CSS</h4>
        <div class="progress-bar">
        <div class="progress" style="width: 90%;"></div>
      </div>
    </div>

    <div class="skill">
        <h4>HTML</h4>
        <div class="progress-bar">
        <div class="progress" style="width: 90%;"></div>
      </div>
    </div>
    
    <div class="skill">
        <h4>Machine Learning</h4>
        <div class="progress-bar">
        <div class="progress" style="width: 66%;"></div>
      </div>
    </div>
                    
    <div class="skill">
        <h4>Statistics</h4>
        <div class="progress-bar">
        <div class="progress" style="width: 95%;"></div>
      </div>
    </div>
                    
    <div class="skill">
        <h4>Problem Solving</h4>
        <div class="progress-bar">
        <div class="progress" style="width: 80%;"></div>
      </div>
    </div>
""", unsafe_allow_html=True)

# Profile Part
st.markdown("""
    <style>
            
        .header-with-image {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }
            
        .header-with-image img {
            width: 40px; /* Adjust size as needed */
            height: 40px; /* Adjust size as needed */
            margin-right: 10px; /* Space between image and text */
        }
            
        .header-with-image h2 {
            margin: 0;
            font-size: 40px;
        } 
    </style>
            
    <div class="header-with-image">
        <img src="https://th.bing.com/th/id/OIP.0miyOJMoCeGLhaeCAYQiDwHaHa?rs=1&pid=ImgDetMain alt="Small Image" //>
        <h2><span style="background-color: #CECECE">Profile</span></h2>
    </div>
            
    <div class="profile-section">
        As a Sri Lankan national, I bring a unique international perspective to my academic and professional pursuits. 
        I am a dynamic and dedicated BSc Computer Engineering student, currently in the 5th semester at the University of Lahore, Pakistan. 
        Proficient in a diverse array of programming languages and tools, including Python, Java, HTML, CSS, PyTorch, TensorFlow, and Pandas. 
        My adeptness in utilizing software development tools such as Visual Studio Code complements my technical skills.
    </div>
            
    <div class="profile-section">
        I possess a keen aptitude for problem-solving, demonstrating the ability to troubleshoot and debug software applications effectively. 
        My exceptional communication skills enable seamless collaboration within team environments and facilitate the clear articulation of technical solutions 
        to non-technical stakeholders. I am passionate about machine learning, statistics, and data analytics, and have a proven track record in these areas, 
        including winning a national silver medal in an Olympiad competition focused on statistics. Exhibiting a proclivity for the rapid assimilation of new technologies, 
        I am committed to continuous learning and professional advancement.
    </div>
""", unsafe_allow_html=True)

#Education Details
st.markdown("""
    <style>
            
        h3,h4{
            margin-top: 5px;
            margin-bottom: 5px;
            padding: 0;
            }

        h4{
            font-size: 20px;
            }

        .header-with-image {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }
            
        .header-with-image img {
            width: 40px; /* Adjust size as needed */
            height: 40px; /* Adjust size as needed */
            margin-right: 10px; /* Space between image and text */
        }
            
        .header-with-image h2 {
            margin: 0;
            font-size: 40px;
        } 
            
    </style>
            
    <div class="header-with-image">
        <img src="https://th.bing.com/th/id/R.dd7e2d99738624cd83015530e43ecc3b?rik=tSnTB8WfO26ljQ&pid=ImgRaw&r=0" alt="Small Image" />
        <h2><span style="background-color: #CECECE">Education</span></h2>
    </div>
            
    <div class="Education-Section">
          <h3>BSc Computer Engineering</h3>
            <h4><em>The University of Lahore, Lahore, Pakistan.</em></h4> 
            <h4><em>Expected Graduation: 2026</em></h4> 
    </div>
            
    <div class="Education-Section">
        <li><b>Current CGPA: 3.87 / 4.00</b></li>
        <li><b>Relevant Coursework:</b> Data Structures, Algorithms, Computer Networks, Artificial Intelligence, Database Management Systems</li>  
        <li><b>Reporting and Documentation:</b>Active member of the Innovation Hub, leading collaborative projects focused on cutting-edge 
            technology solutions.</li>
        <li><b>Technical Skills: </b> Proficient in Python, Java, HTML, CSS, PyTorch, TensorFlow, Pandas, and MATLAB, with hands-on experience in 
            building and deploying machine learning models.</li>
    </div>
            
    <div class="Education-Section">
          <h3>GCE A-Levels in Physical Sciences</h3>
            <h4><em>Richmond College, Galle, Sri Lanka.</em></h4> 
            <h4><em>Completed: 2022</em></h4>  
    </div>
            
    <div class="Education-Section">
            <li><b>Main Subjects:</b> Applied Mathematics, Pure Mathematics, Chemistry, Physics</li>
            <li><b>Academic Excellence:</b> Demonstrated strong analytical and quantitative skills through rigorous coursework in mathematics 
            and sciences.</li>
            <li><b>Problem-Solving Skills:</b>  Developed a solid foundation in problem-solving and critical thinking, particularly in complex 
            mathematical and scientific concepts.</li>
            <li><b>Achievements:</b> Gained comprehensive knowledge in physical sciences, which laid the groundwork for advanced studies in
            Computer Engineering and Machine Learning.</li>
    </div><br>
""",unsafe_allow_html=True)

#Employment Details
st.markdown("""
    <style>
            
        h3,h4{
            margin-top: 5px;
            margin-bottom: 5px;
            padding: 0;
            }

        h4{
            font-size: 20px;
        }
            
        .header-with-image {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }
            
        .header-with-image img {
            width: 40px; /* Adjust size as needed */
            height: 40px; /* Adjust size as needed */
            margin-right: 10px; /* Space between image and text */
        }
            
        .header-with-image h2 {
            margin: 0;
            font-size: 40px;
        }      
    </style>
            
    <div class="header-with-image">
        <img src="https://www.pngfind.com/pngs/m/378-3782102_group-of-employees-icon-hd-png-download.png" alt="Small Image" />
        <h2><span style="background-color: #CECECE">Employment History</span></h2>
    </div>

    <div class="Employment-Section">
          <h3>Intern, ERP Department</h3>
            <h4><em>University of Lahore</em></h4> 
            <h4><em>June 2024 to Aug 2024</em></h4> 
    </div>
            
    <div class="Employment-Section">
        <li><b>File Duplication Analysis:</b> Executed comprehensive file duplication detection and resolution strategies, significantly enhancing data 
        integrity and system performance. Applied advanced algorithms and data management tools to identify redundant files, streamline data 
        processes, and reduce storage overhead.</li>
        <b><li>Data Management:</b> Collaborated with the IT team to develop and implement solutions for optimizing data storage and retrieval, 
        contributing to overall system efficiency and reliability.</li>  
        <b><li>Reporting and Documentation:</b> Generated detailed reports on duplication findings and recommended improvements, aiding in decision-making
        and strategic planning for data management practices.</li>
    </div>
            
    <div class="Employment-Section">
          <h3>Intern, Neemiracle Technologies Pvt.Ltd</h3>
            <h4><em>Machine Learning (Remote)</em></h4> 
            <h4><em>Aug 2024 to Sep 2024</em></h4>  
    </div>
            
    <div class="Employment-Section">
            <li><b>Model Development & Optimization:</b> Collaborating on the development and fine-tuning of machine learning models for real-world applications, 
            focusing on predictive analytics and data-driven decision-making.</li>
            <li><b>Data Preprocessing & Feature Engineering:</b> Engaging in advanced data preprocessing techniques, including feature engineering and data augmentation, 
            to enhance model accuracy and performance.</li>
            <li><b>Research & Implementation:</b> Conducting research on state-of-the-art machine learning algorithms and implementing them to solve complex business 
            challenges, ensuring the application of cutting-edge methodologies.</li>
            <li><b>Cross-Functional Collaboration:</b> Working closely with data scientists, engineers, and domain experts to integrate machine learning solutions into
            existing systems, contributing to the overall innovation strategy of the company.</li>
            <li><b>Project Management:</b> Taking ownership of specific projects, from initial data exploration to model deployment, demonstrating leadership in driving 
            key machine learning initiatives.</li>
    </div>
            
    <div class="Employment-Section">
          <h3>Intern, YoungDev Interns</h3>
            <h4><em>Python Developer (Remote)</em></h4> 
            <h4><em>Aug 2024 to Sep 2024</em></h4>  
    </div>
            
    <div class="Employment-Section">
            <li><b>Backend Development:</b> Contributing to the development of backend systems using Python, focusing on building robust, scalable, and efficient APIs
            and services.</li>
            <li><b>Automation Scripting:</b> Writing automation scripts to streamline repetitive tasks, improving efficiency and reducing manual workload across various
            departments.</li>
            <li><b>Code Optimization:</b> Enhancing existing Python codebases by implementing best practices, optimizing performance, and ensuring code maintainability 
            and readability.</li>
            <li><b>Testing & Debugging:</b> Conducting thorough testing and debugging of applications, ensuring functionality, reliability, and bug-free deployments in 
            production environments.</li>
            <li><b>Version Control:</b> Actively managing and collaborating on projects using Git, adhering to version control practices and contributing to a shared 
            codebase in a team environment.</li>
    </div>
            
    <div class="Employment-Section">
          <h3>Intern, CodeAlpha</h3>
            <h4><em>Data Science (Remote)</em></h4> 
            <h4><em>Aug 2024 to Sep 2024</em></h4>  
    </div>
            
    <div class="Employment-Section">
            <li><b>Data Analysis & Visualization:</b> Analyzing large datasets to uncover patterns, trends, and insights, using tools like Python, Pandas, and Matplotlib.
            Developing interactive dashboards to communicate findings to stakeholders.</li>
            <li><b>Machine Learning Implementation:</b> Assisting in the development and deployment of machine learning models, focusing on predictive analytics, classification, 
            and clustering techniques.</li>
            <li><b>Data Cleaning & Preparation:</b> Conducting thorough data cleaning, transformation, and preparation to ensure high-quality datasets for analysis and model
            training, leading to improved model performance.</li>
            <li><b>Collaborative Projects:</b> Working alongside senior data scientists and engineers on collaborative projects, contributing to the design and implementation 
            of data-driven solutions that align with business objectives.</li>
            <li><b>Technical Documentation:</b> Creating detailed documentation of processes, algorithms, and model performance, facilitating knowledge sharing and future project
            scalability.</li>
    </div>
""",unsafe_allow_html=True)