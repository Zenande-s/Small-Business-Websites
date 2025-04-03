from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Small Business Websites SA</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin: 20px; }
            nav ul { list-style-type: none; padding: 0; }
            nav ul li { display: inline; margin: 10px; }
            section { margin: 20px 0; }
            form input, form textarea, form button { display: block; margin: 10px auto; width: 80%; }
        </style>
    </head>
    <body>
        <header>
            <h1>Affordable Websites for Small Businesses in South Africa</h1>
            <nav>
                <ul>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#portfolio">Portfolio</a></li>
                    <li><a href="#pricing">Pricing</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </header>
        
        <section id="hero">
            <h2>Get Your Business Online Today!</h2>
            <p>Professional, fast, and affordable websites designed for South African businesses.</p>
            <a href="#contact">Get a Free Quote</a>
        </section>
        
        <section id="services">
            <h2>Our Services</h2>
            <ul>
                <li>Business Websites</li>
                <li>E-commerce Stores</li>
                <li>SEO & Digital Marketing</li>
                <li>Website Maintenance</li>
            </ul>
        </section>
        
        <section id="portfolio">
            <h2>Our Work</h2>
            <p>Check out websites we've built for small businesses.</p>
        </section>
        
        <section id="pricing">
            <h2>Pricing</h2>
            <p>We offer flexible pricing to suit your business needs.</p>
        </section>
        
        <section id="contact">
            <h2>Contact Us</h2>
            <p>Get in touch to start your website today.</p>
            <form action="/submit" method="post">
                <input type="text" name="name" placeholder="Your Name" required>
                <input type="email" name="email" placeholder="Your Email" required>
                <textarea name="message" placeholder="Your Message" required></textarea>
                <button type="submit">Send Message</button>
            </form>
        </section>
        
        <footer>
            <p>&copy; 2025 Small Business Websites SA | All rights reserved.</p>
        </footer>
    </body>
    </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    return f"Thank you, {name}. We have received your message and will be in touch soon."

if __name__ == '__main__':
    app.run(debug=True)
