# Friendly_Gadget
ALX-Project_Portfolio
# Friendly Gadget
![GitHub repo size](https://img.shields.io/github/repo-size/Yusuf-R/Friendly_Gadget)
![GitHub issues](https://img.shields.io/github/issues/Yusuf-R/Friendly_Gadget)
![GitHub Repo stars](https://img.shields.io/github/stars/Yusuf-R/Friendly_Gadget?logo=github&style=flat)
![GitHub forks](https://img.shields.io/github/forks/Yusuf-R/Friendly_Gadget?logo=github&style=falt)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Yusuf-R/Friendly_Gadget?logo=github)

![banner](web_dynamic/static/assets/img/cover.png)

## Overview

Friendly Gadget is a web-based platform designed to help people understand your gadget choices. It will be your one point of reference for a complete informative guide about a product or service of your mobile or computer devices

## The Story
Introducing our revolutionary web application FriendlyGadget, designed to transform the way you choose your mobile devices. Picture this: a world where selecting the perfect device is a seamless, informed, and exhilarating experience. It all began with a realization - a common thread among conversations with friends, colleagues, and peers. The need for a mobile device, be it an upgrade or a fresh start, was apparent. Yet, there was always a gap, a disconnect between understanding the features of a device and envisioning its optimal performance in real-world applications.

I vividly recall the quest to find the ideal mobile device for my dear friend. This decision was monumental, meant to cater to her every desire, encompassing aesthetics, performance, and application capabilities. The journey through countless device options was akin to a thrilling rollercoaster ride. With so many choices and limited knowledge of how their features would fare in diverse application scenarios, the process became arduous. It demanded time, consideration, and meticulous evaluation of various factors.

Finally, after extensive deliberation, we arrived at a decision. Yet, as the dust settled, I couldn't help but reflect on the time-consuming nature of the process. The pace of decision-making was nerve-wracking thus, we need a solution to help Fastrack user decision.

This led us to create a groundbreaking solution FreindlyGadget - a web-based application that streamlines access to vital information and application resources. Say goodbye to hours of research and uncertainty. Say hello to a future where confidence meets efficiency. Welcome to our game-changing mobile device selection experience.

Front End
* HTML
* CSS
* JavaScript
* BoostStrap CSS Framework for developing responsive and mobile-first websites.

RESTful API
* GET, POST, PUT and DELETE requests handled
* CRUD manipulation through RESTful API

Relational Database
* MySql Handled with ORM (SQLAlchemy)
* Model system with base model handling identification
* Many to many relationships for users and rewards

Server / Deployment
* Nginx / Gunicorn
* Ubuntu 20.04

## Features

The Friendly_Gadget APP includes the following key features:

1. **Get the Best Device:** Users can get the device that is suitable for their purposes with ease, by displaying the search results based on their requirements

2. **Identify your Device:** Users can view the device's specifications and capabilities and identify each characteristic separately.




# Installation
## Dependencies
This application is written in Python and requires Python 3.8 or later to run correctly.

## Getting Started

Clone this git repository. If you are a GNU/Linux user, you could copy and paste the
following command to clone and change the working directory into the root of this project:

```sh
git clone https://github.com/Yusuf-R/Friendly_Gadget && cd Friendly_Gadget
```

Otherwise, clone the repository as you'd like and change the working directory into
the root of the project.
## Command Interpreter (The Console)

The command interpreter is a command-line interface that allows users to interact
with the **Freindly_Gadget** system. It provides a set of commands for managing the various
aspects of the system, such as creating and managing Brands, Models and so on.

### Starting the Command Interpreter

To start the command interpreter, navigate to the root of the project if not already there
and run the following command:

```sh
./console.py
```

This will start the command interpreter and you will be presented with a prompt,
`[FreindlyGadget]: `, where you can start entering commands.

### Using the Command Interpreter

The command interpreter provides a set of commands for managing the various aspects
of the **Friendly_Gadget** clone system. Some of the available commands include:

| Command         | Description                                                       | Usage                                                                 |
| ---------       | ----------------------------------------------------------------- | --------------------------------------------------------------------- |
| `create_model`  | Create a new instance of a class                                  | `create_model <class_name>`                                           |
| `show`          | Show the details of a specific instance of a class                | `show <class_name> <instance_id>`                                     |
| `all`           | Display the details of all instances or all instances of a class  | `all` or `all <class_name>`                                           |
| `delete`        | Delete a specific instance of a class                             | `delete <class_name> <instance_id>`                                   |
| `update`        | Update the attribute value for a given instance of a class        | `update <class_name> <class_id> <attribute_name> "<attribute_value>"` |
| `quit`          | Quits the command interpreter                                     | `quit`                                                                |                                                                   |

> The interpreter can also be terminated by hitting the `EOF` key combination.

To use a command, simply type the command followed by any required arguments at the prompt
and hit enter.

For example, to create a new instance of the `Brand` class, you would run the following command:

```sh
[FreindlyGadget]: create_brand Apple
```

To show the details of a specific instance of a class, you would run the following command,
where `<class_id>` is the ID of the instance you want to show:

```sh
[FreindlyGadget]: show <class> <id>
```

Some interpreter commands can also be processed when used as suffixes to a class name:

- `show`: `<class_name> ("<instance_id>")`

Example:

> ```sh
> [FreindlyGadget]: show Brand f0ca205f-31dc-40e4-ac82-09a83d75bcaa
> ```
>
> to print a representation of the Brand with id `f0ca205f-31dc-40e4-ac82-09a83d75bcaa`

> to get the instances of the class `Brand`

- `all`: `<class_name>`

Example:

> ```sh
> [FreindlyGadget]: all Brand
> ```
>
> to print all instances of the class `City`

- `delete`: `<class_name> "<instance_id>"`

Example:

> ```sh
> [FreindlyGadget]: delete Brand "f0ca205f-31dc-40e4-ac82-09a83d75bcaa"
> ```
>
> to delete the instance of class `Brand` with id `f0ca205f-31dc-40e4-ac82-09a83d75bcaa`

- `update`: `<class_name> ("<instance_id>", "<attribute_name>", "<attribute_value>")`

Example:

> ```sh
> [FreindlyGadget]: update Brand ("f0ca205f-31dc-40e4-ac82-09a83d75bcaa", "brand_name", "Infinx")
> ```
>
> to update the attribute called `brand_name` of the instance of `Brand` class with id `f0ca205f-31dc-40e4-ac82-09a83d75bcaa`

The `.update` extension also works with a dictionary of attribute name(s) and value(s)

For a full list of all commands and their usage, run the following command:

```sh
[FreindlyGadget]: help
```

or

```sh
[FreindlyGadget]: help <command>
```

for a help doc on a specific command.

## Usage

1. **Search for a suitable Device:**
   - You will be great with your landing page 
   - Click on “Get Start” and you will be directed to the search section form 
   - Choose your device category (PC or mobile) and start defining your specific purpose and purposes.
   - You can also explore the latest models and view their details in our latest Models

2. **Search and preview:**
     - Matching search results appear and simplified information for the device description is displayed.
     - Use the “Read More” feature to see product details.


## Authors

The [AUTHORS](https://github.com/Yusuf-R/Friendly_Gadget/blob/main/AUTHORS)
file at the root of the repository lists all individuals who were part of the project
from conception. Their full names, links, and contact information are listed below:

<details>
    <summary>Yusuf Abdulwasiu Tunde</summary>
    <ul>
    <li><a href="https://www.github.com/Yusuf-R">GitHub</a></li>
    <li><a href="https://www.linkedin.com/in/abdulwasiu-yusuf-10044299/">Linkedin</a></li>
    <li><a href="mailto:y.abdulwasiu@gmail.com">Gmail</a></li>
    </ul>
</details>
<details>
    <summary>Saria Mohammed</summary>
    <ul>
    <li><a href="https://www.github.com/saria-mohi">GitHub</a></li>
    <li><a href="https://www.linkedin.com/in/saria-mohi-aldein-mohammed-b17630137/">Linkedin</a></li>
    <li><a href="mailto:saria.m.mohammed@gmail.com">Gmail</a></li>
    </ul>
</details>
