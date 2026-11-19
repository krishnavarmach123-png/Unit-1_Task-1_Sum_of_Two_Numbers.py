<!DOCTYPE html>
<html>
<head>
    <title>My Portfolio</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background: #f4f4f9;
            color: #333;
        }

        nav {
            background: #483d8b;
            padding: 18px;
            display: flex;
            justify-content: space-between;
            color: white;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin-left: 18px;
        }

        .home {
            background: #b0e0e6;
            text-align: center;
            padding: 45px;
        }

        .home img {
            width: 110px;
            height: 110px;
            border-radius: 50%;
            border: 4px solid white;
            object-fit: cover;
        }

        h1 {
            color: #191970;
            margin: 15px;
        }

        section {
            padding: 35px;
            text-align: center;
        }

        h2 {
            color: #483d8b;
            margin-bottom: 20px;
        }

        .skills {
            background: #fff3b0;
        }

        .skill {
            display: inline-block;
            background: white;
            padding: 18px 30px;
            margin: 8px;
            border-radius: 8px;
            box-shadow: 0 2px 6px #ccc;
        }

        .projects {
            background: #e6e6fa;
        }

        .contact {
            background: #b0e0e6;
        }

        footer {
            background: #483d8b;
            color: white;
            text-align: center;
            padding: 15px;
        }
    </style>
</head>

<body>

    <nav>
        <b>My Portfolio</b>
        <div>
            <a href="#about">About</a>
            <a href="#skills">Skills</a>
            <a href="#education">Education</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </div>
    </nav>

    <div class="home">
        <img src="profile.PNG" alt="My Photo">
        <h1>P Bhavya Prasanna</h1>
        <p>Aspiring Web Developer | B.Tech CSE Student</p>
    </div>

    <section id="about">
        <h2>About Me</h2>
        <p>
            I am a first-year B.Tech student at NRI University.
            I am interested in web development and technology.
            I enjoy learning new skills and creating websites.
        </p>
    </section>

    <section class="skills" id="skills">
        <h2>My Skills</h2>
        <div class="skill">HTML</div>
        <div class="skill">CSS</div>
        <div class="skill">Python</div>
        <div class="skill">Problem Solving</div>
        <div class="skill">Communication</div>
    </section>

    <section id="education">
        <h2>Education</h2>
        <h3>B.Tech - CSE Core</h3>
        <p>NRI University, Agiripalli</p>
        <p>Intermediate - Completed</p>
        <p>10th Class - Completed</p>
    </section>

    <section class="projects" id="projects">
        <h2>My Projects</h2>
        <div class="skill">
            <h3>Portfolio Website</h3>
            <p>Created using HTML and CSS</p>
        </div>
        <div class="skill">
            <h3>Registration Form</h3>
            <p>Designed using HTML</p>
        </div>
    </section>

    <section class="contact" id="contact">
        <h2>Contact Me</h2>
        <p>Email: yourmail@gmail.com</p>
        <p>Location: Andhra Pradesh, India</p>
    </section>

    <footer>
        <p>© 2026 Bhavya | My Portfolio</p>
    </footer>

</body>
</html>