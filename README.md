<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/pantercp">
    <img src="https://github.com/pantercp/Personal_Portfolio_Website/blob/master/images/logo2.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">NinetyNine</h3>

  <p align="center">
    A daily desktop wallpaper - aimed at inspiring and promoting productivity
    <br />
    <a href="https://github.com/pantercp/desktop-dashboard.git"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/pantercp/desktop-dashboard.git">View Demo</a>
    ·
    <a href="https://github.com/pantercp/desktop-dashboard/issues">Report Bug</a>
    ·
    <a href="https://github.com/pantercp/desktop-dashboard/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
          <li>
      <a href="#stages-of-the-program">Stages Of The Program</a>
                         <ul>
        <li><a href="#productivity-dashboard">Productivity Dashboard</a></li>
      </ul>
             <ul>
        <li><a href="#inspirational-image">Inspirational Image</a></li>
      </ul>
             <ul>
        <li><a href="#desktop-maker">Desktop Maker</a></li>
      </ul>
                   <ul>
        <li><a href="#wallpaper-update">Wallpaper Update</a></li>
      </ul>
          <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
        <li>
      <a href="#personalisation">Personalisation</a>
      <ul>
        <li><a href="#images">Images</a></li>
        <li><a href="#inspiration">Inspiration</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

NinetyNine creates a completely unique desktop wallpaper every day to keep you inspired and is comprised of an inspirational image in the centre, with space to the left side to organise your desktop shortcuts and temporary files. To the right side of the image there is a space to be utilised for what I refer to as your personal dashboard.

<img src="https://github.com/pantercp/desktop-dashboard/blob/master/examples/example-1.jpg" alt="Logo" width="100%" height="100%">

<p align="center">(<a href="#readme-top">back to top</a>)</p>

<!-- STAGES OF THE PROGRAM -->

## Stages Of The Program

Once the program is correctly installed and configured, running the program goes through the following sequence.

### Productivity Dashboard

The program first enters the "Productivity Dashboard" which enables you to manage your personal objectives. Here you can view, add, edit, delete and complete any personal objectives that you have. The objectives are all stored within a csv file which records the following for each of them: Date, Category, Objective, Deadline, Complete (date).

Adding an objective -  Records todays date automatically, whilst Category, Objective and Deadline are all requested user inputs, and Complete is automatically set to "FALSE".

Completing an objective - This function asks you to define which objective you have completed and to then enter the completion date. Once an Objective has a complete date it is treated as a Milestone.

At the later stage - **Desktop Maker**, the objectives csv file is then used to access this information and then draws these objectives and milestones onto the desktop wallpaper.

### Inspirational Image

This part of the program solely creates the image in the centre of the wallpaper and ensures a completely unique image every time you run it. The program accesses two csv files and a folder of images. One is a list of 99 different things to be grateful for and 99 affirmations, whilst the other csv is comprised of the 99 names of Allah along with a translation for each name. *Note these variables are not limited to 99.

Every time the program runs it uses the **choice** module to randomly choose: an image, affirmation, something to be grateful for and a name of Allah. It then compiles these choices and creates a completely unique image for inspiration.

<img src="https://github.com/pantercp/desktop-dashboard/blob/master/examples/example-2.jpg" alt="Logo" width="30%" height="30%"> <img src="https://github.com/pantercp/desktop-dashboard/blob/master/examples/example-3.jpg" alt="Logo" width="30%" height="30%"> <img src="https://github.com/pantercp/desktop-dashboard/blob/master/examples/example-4.jpg" alt="Logo" width="30%" height="30%">

### Desktop Maker

To give the program a wallpaper image to work from I created a 1920x1080 image in Canva, which gives the desired background image and defines space on the left hand side for placing desktop shortcuts and files.

<img src="https://github.com/pantercp/desktop-dashboard/blob/master/examples/template.jpg" alt="Logo" width="50%" height="50%">

At this point the program then retrieves the image created from **Inspirational Image** and pastes it onto the template wallpaper (shown above).  

After this the **Desktop Maker** draws all of the information shown to the right of the centre image.  Which is split into two main sections - personal and productivity. 

The productivity information is found in objectives.csv, it enters this file and draws all of the outstanding Objectives onto the template wallpaper along with the amount of days remaining until the deadline for completion. Then the three most recently completed Objectives are then drawn on the wallpaper as Milestones.

<img src="https://github.com/pantercp/desktop-dashboard/blob/master/examples/example-5.jpg" alt="Logo" width="30%" height="30%"> 

The personal information is more for the individuals interests and is powered using the appropriate api's for the desired content. My version was designed to show the days Prayer Times, Local Weather, Market Prices and my football team's next Fixture.

<img src="https://github.com/pantercp/desktop-dashboard/blob/master/examples/example-6.jpg" alt="Logo" width="30%" height="30%">

### Wallpaper Update

Now that the days wallpaper has been created the final stage is where the program changes the desktop wallpaper to the image found in the **output** folder. Voila, you have a new desktop wallpaper (like image below) designed specifically to organise and inspire your day.

<img src="https://github.com/pantercp/desktop-dashboard/blob/master/examples/example-7.jpg" alt="Logo" width="100%" height="100%">

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Prerequisites
### Installation

## Personalisation

### Images
### Inspiration

<!-- CONTACT -->
## Contact

Christian Panter - https://www.linkedin.com/in/christianpanter/ - cjpixeluk@gmail.com

Project Link: [https://github.com/pantercp/desktop-dashboard.git](https://github.com/github_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []() Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Book by Al Sweigart
* []() Python for Absolute Beginners | Python Beginner to Pro 2023 - Udemy Course

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
