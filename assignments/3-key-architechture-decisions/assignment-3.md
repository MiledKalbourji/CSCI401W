# Key Architectural Decisions

## Table of Contents

- [Directions](#directions)
- [1. Introduction](#1-introduction)
  - [1.1. Purpose](#11-purpose)
- [2. System Overview](#2-system-overview)
- [3. Technical Choices](#3-technical-choices)
  - [3.1. Frontend Framework](#31-frontend-framework)
  - [3.2. Backend Framework](#32-backend-framework)
  - [3.3. Database System](#33-database-system)
- [4. Other Considerations](#4-other-considerations)
  - [4.1. Team Skills and Learning](#41-team-skills-and-learning)
  - [4.2. Community and Support](#42-community-and-support)
  - [4.3. Future Adaptability](#43-future-adaptability)
- [5. Decision Log](#5-decision-log)

## Directions:

This assignment is designed to guide you in understanding the foundational aspects of your project. Remember, in software engineering, understanding the "why" behind decisions is often as important as the decisions themselves. As you navigate these early stages of your coding journey, focus on grasping the core reasons behind each choice, and use this document to record and reflect on those reasons.

---

## 1. Introduction

### 1.1. Purpose

This document provides insight into the decisions made on the frameworks and coding languages used in the Teacher.io project.

---

## 2. System Overview

Teacher App is an app designed to track student truancy through attendance utilities.  The app gives teachers a UI To take attendance and alert parents via text message if their student is absent.  It also allows administrators to keep track of truancy rates within a school or district.

---

## 3. Technical Choices

### 3.1. Frontend Framework

We will set up a simple HTML front end.  It is simple to connect to Django, and all of our team members have experience coding in HTML. There are several other frameworks out there that we had trouble connecting which is why we ultimately ended up here.

### 3.2. Backend Framework

We will be using Django. The framework is compatible with Python which provides a wide variety of libraries. Our instructor is also familiar with it which will provide a helpful resource if we run into obstacles.  Choosing Django also allows us to use one framework for both the front end and the back end. Django has an emphasis on security features. Django is also useful for implementing push notifications.

### 3.3. Database System

We will be using MongoDB.  Mohammed has some familiarity with it and it provides the necessary functionality for what we are looking for.  Mongo is also compatible with Excel spreadsheets, which is the format of some of the mock data that Miled has found.

---

## 4. Other Considerations

### 4.1. Team Skills and Learning

Mohammed has experience working with MongoDB which was a factor in choosing that for our database framework. We are all looking forward to learning Django.

### 4.2. Community and Support

Django is a very well documented framework that has a lot of available resources.  Our instructor also has experience in Django which will give us another resource. MongoDB is also a very well documented framework with a lot of available resources.

### 4.3. Future Adaptability

We hope to develop our program into a desktop app eventually, which should be a relatively easy task. The base of our program will provide most of the necessary functionality, and scaling it will just require extending the system, especially given the fact that we are using a common set of frameworks.

---

## 5. Decision Log

Here, you'll log key decisions made and the rationale behind them. Here's an example:

| Date       | Decision                                 | Reasoning                                                                                                           |
|------------|------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| 2024-02-29 | Chose Django as our frontend and backend framework.   | There are a lot of available resources on Django, and it has the capability to serve as both the front end framework and the back end framework. |
| 2024-02-29 | Chose MongoDB as our database framework.              | There are a lot of available resources on MongoDB, as well as resources on using it in conjuction with Django. |
| 2024-03-25 | Changed from Django to Tinker for our front end.      | We were having trouble installing and getting Django working for our GUI, so we changed to Tinker. |
| 2024-04-15 | Changed from Tkinter to Dash for our front end.       | We found out that Tkinter wasn't able to be used for a web app which is what we were hoping to develop.  Dash is another Python framework so we figured it would be simple to make the switch. |
| 2024-04-25 | Changed from Dash to a simple HTML GUI                | We were not able to connect dash to our Django because of a Flask implementation, so we decided to create a simple HTML GUI due to the time constraints. |

Note: As you progress, keep adding to this log. It will not only help you track your decisions but also offer insights into your evolving
