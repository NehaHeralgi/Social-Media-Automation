# Social-Media-Automation
Social Media Automation is an automation tool which automates Social media handles such as Instagram, Facebook and Twitter


## Description

With the rising use of technology prevalent in the past few decades, there has been a significant
increase in the usage of social media for not only entertainment purposes, but also for marketing
strategies and other valuable opportunities. However, there a multiple social media platforms
for one particular organisation or company and it becomes a difficult and mundane task to post
the same information on all of the platforms. Celebrities, VIPs, Sportspersons and other people
of powerful statuses also do not find the time to improve their engagement with their target
audience on Social Media. It also consumes unnecessary efforts, reduces efficiency and causes
the loss of productivity that would have been achieved at the same time.

This is where Social Media Automation comes in. It is a simple, straightforward way to have
consistent digital marketing or digital campaigns. It saves a lot of time, helps use that time to
improve engagements, reduces efforts required and maintains consistency. Digital marketing
gets a great boost through Automation, which helps to improve the organisation and widen its
reach.


## Getting Started

# Requirements

The code would be divided into two parts:

(i) Automation: This would allow various social media tasks to happen using browser
APIs through Selenium and using Instabot module in Python. The inputs required for
these tasks would be given by the user through the interface created.

(ii) Interface: This would be created with the help of the Tkinter module in Python. The
Tkinter module is easy to use and provides a variety of features that help make the
interface look attractive to use and handle by users.

# System Design

![Screenshot (947)](https://user-images.githubusercontent.com/91747940/141611014-ed651dab-2a3a-48bd-8c68-c76c16603710.png)

The user would first access the automation tool through the interface. The interface would ask
them to choose which social media platform they would like to perform automation in, and be
given the options of Instagram, Facebook and Twitter.

According to the option chosen and the inputs given, they are taken to a separate page for the
particular social media where automation is performed. Then they choose from the options of:

* uploading a post
* liking/unliking
* commenting and
* following/unfollowing

After selecting the options and providing the interface with the required information, the
automation tool will begin its work to achieve the user’s desired goal. 

# Modular Design

The code will be divided into 3 modules for effectiveness and reusability. These are:

![Screenshot (948)](https://user-images.githubusercontent.com/91747940/141611069-40b7da25-e39b-403f-9ebc-11c43411d7a4.png)

The respective modules of Instagram, Facebook and Twitter in the code would appear as
functions, entailing in them all the required features to make automation possible using
Selenium and Instabot in Python.

Based on the inputs given by the user, the automation would be performed accordingly and
outputs will be visible on the particular platform.

# Interface SCREENSHOTS:

The introductory interface presents a screen that encourages the user to try automating their
posts. It then shows them three buttons as options to click, which are the platforms Instagram,
Facebook and Twitter which the user can select.

![Screenshot (957)](https://user-images.githubusercontent.com/91747940/141613171-6bbbbe8d-a3d9-4045-bc25-3c9a1f311347.png)

![Screenshot (958)](https://user-images.githubusercontent.com/91747940/141613211-164ab03b-8069-4d9e-8984-1bea6a71b3f6.png)

![Screenshot (959)](https://user-images.githubusercontent.com/91747940/141613221-06da5482-7437-4766-94e9-e1e5e75bfdc2.png)

![Screenshot (960)](https://user-images.githubusercontent.com/91747940/141613230-e79518ef-cfdb-45c3-b459-41b1b3b5adb2.png)

Upon clicking the Facebook button as a choice, the user is introduced to a new page:

![Screenshot (961)](https://user-images.githubusercontent.com/91747940/141613248-dca60baa-47ce-48b0-9765-b0f1d882e952.png)

Upon clicking the Twitter button as a choice, the user is introduced to a new page:

![Screenshot (962)](https://user-images.githubusercontent.com/91747940/141613251-6645a532-d47e-4016-ac59-fb14286dfce1.png)

# System Requirments
Libraries:
* Selenium
* Tkinter
* Instabot
* pyautogui
* Latest ChromeWebdriver

## Execution
Add the latest xpaths and css selectors of social media websites to avoid errors
