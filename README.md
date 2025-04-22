![GitHub](https://img.shields.io/github/license/namansehwal/EcoMart)
![GitHub repo size](https://img.shields.io/github/repo-size/namansehwal/EcoMart)

# EcoMart 
[Demo Video :movie_camera: ](https://youtu.be/xaA5xjPM2vM?list=LL)  

EcoMart is an e-commerce platform focused on environmentally friendly and sustainable products. This platform aims to connect consumers with products that have a positive impact on the environment.

## Application Snapshots 

<div class="carousel">
    <details> <summary>Admin's Dashboard</summary>
  <img src="https://raw.githubusercontent.com/namansehwal/EcoMart/main/static/admin_page.png" alt="Image 1" width='80%'>
            </details>
 <details> <summary>Homepage</summary> <img src="https://raw.githubusercontent.com/namansehwal/EcoMart/main/static/user.png" alt="Image 2"  width='80%'>   </details>
  <details><summary>Product Card</summary> <img src="https://raw.githubusercontent.com/namansehwal/EcoMart/main/static/product.png" alt="Image 3"  width='80%'>   </details>

</div>



## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

EcoMart is built with the goal of promoting eco-friendly products and practices. It provides a user-friendly interface for users to explore, search, and purchase products that align with sustainability values. Whether you're a conscious consumer or a seller of sustainable products, EcoMart provides a platform to connect and contribute to a greener future.

## Features

- **Product Listings:** Browse through a wide range of sustainable products.
- **Search and Filters:** Easily find products using search and filtering options.
- **User Accounts:** Create and manage your account for a personalized experience.
- **Shopping Cart:** Add and remove products from your cart before making a purchase.
- **Seller Dashboard:** For sellers to manage their products and inventory.
- **Order History:** Track your order history and delivery status.

## [API Documentation](https://github.com/namansehwal/EcoMart/blob/main/api_documentation.md)



# :rocket: Quick Start

**Run the site locally**

### Installation

To set up EcoMart locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/namansehwal/EcoMart.git
    cd EcoMart
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```
 5. To run flask server
```bash
python application.py
```   
### :open_file_folder: What's inside?

A quick look at the folder structure of this project.

    .
    APPDEV-PROJECT/
    ┣ static/
    ┃ ┣ assets/
    ┃ ┣ styles/
    ┣ templates/
    ┃ ┣ admin/
    ┃ ┣ login/
    ┃ ┗ user/
    ┣ admin_routes.py
    ┣ api.py
    ┣ api_methods.yaml
    ┣ application.py
    ┣ authentication.py
    ┣ database.sqlite3
    ┣ README.md
    ┣ requirements.txt
    ┣ user_routes.py
    ┗ vault.py

## Contributing 🧑‍🤝‍🧑


If you'd like to contribute to the project, here are the steps:

1. Fork the Project.
2. Create your Feature Branch: `git checkout -b feature/YourFeature`
3. Commit your Changes: `git commit -m 'Add some amazing feature'`
4. Push to the Branch: `git push origin feature/YourFeature`
5. Open a Pull Request.

## License 🏛️

This project is licensed under the MIT License.

## Contact 🤙

Connect with the project creator for any questions or feedback:

- Name: Naman Sehwal
- Email: namansehwal@gmail.com
- GitHub: [@namansehwal](https://github.com/namansehwal)
- LinkedIn: [Naman Sehwal](https://www.linkedin.com/in/namansehwal/)

Feel free to explore the code and contribute to make this app even better! 😊
