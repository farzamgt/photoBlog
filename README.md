# photoBlog

### About

&nbsp;&nbsp;&nbsp;&nbsp;photoBlog is a demo project showcasing my skills in Django, HTML, CSS, and Bootstrap. This simple blog platform includes a fully functional login system, allowing users to register, log in, and interact with the content. Users can view photos posted by others, leave comments, and manage their own posts.

### Features

&nbsp;&nbsp;&nbsp;&nbsp;User Authentication: Register and log in to access the full features of the blog.
Post Management: Create, edit, and delete your own posts.
Commenting: Leave comments on posts and manage your own comments.
Responsive Design: Optimized for various display sizes, including mobile, tablet, and desktop.

### Technologies Used

Django:  
&nbsp;&nbsp;&nbsp;&nbsp;The backend framework used to manage the application logic and database interactions.

HTML & CSS:  
&nbsp;&nbsp;&nbsp;&nbsp;The core technologies for structuring and styling the web pages.

Bootstrap:  
 &nbsp;&nbsp;&nbsp;&nbsp;A frontend framework for building responsive and modern interfaces.

## Installation

- Clone the repository:

git clone https://github.com/farzamgt/photoBlog.git

- Navigate to the project directory:

cd photoBlog

- Install the required dependencies:

pip install -r requirements.txt

- Apply the migration to your database by running:

python manage.py migrate

- Run the development server:

python manage.py runserver

&nbsp;&nbsp;&nbsp;&nbsp;You can create a superuser to act as the admin of this blog. The superuser can manage the blog by adding more categories, managing users, and overseeing posts.

- Execute the following command to create a superuser:

python manage.py createsuperuser

### Usage

Once the development server is running, you can access the application at http://localhost:8000/. You can register a new account or log in with an existing one to start exploring and interacting with the blog.
