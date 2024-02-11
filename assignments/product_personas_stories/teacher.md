# Product Personas and Stories

## Team: A

Table of Contents

- [Product Definition](#product-definition)
- [Vision Statement](#vision-statement)
- [Product Personas](#product-personas)
- [Product Scenarios](#product-scenarios)
- [User Stories](#user-stories)
- [User Experience](#user-experience)

## Product Definition

**Teacher** App is a cutting edge application software tailored to middle school and high schools, focused with the issue of attacking the issue of students skipping class and student truancy. Accessible through mobile devices and web apps it offers a very simple interface for teachers to monitor attendance in each class. Teacher App is committed to improving student attendance and overall academic success in middle school and high school.

## Vision Statement

FOR financial compliance professionals WHO need to look into the source/destination of funds transferred using the blockchain. **Blockr.io** is a web-based SaaS application THAT permits compliance teams to derive insights from the blockchain and mitigate financial crime risk. UNLIKE other forensic analysis tools, OUR PRODUCT provides state of the art technology that empowers compliance teams to make better risk management decisions.

## Product Personas

- **Persona 1**: Truant student, (beneficiary) truant students are children who often skip class leading to them failing the class. These are students who have parents that aren’t engaged with the child’s education.
- **Persona 2**: Single Parent, (secondary user) not the primary users, they are the ones to receive text notifications from the teachers if their child had bunked that class on that day.
- **Persona 3**: School District (customer/buyer) In the Gotham city district , we have below average attendance throughout the school system. Teacher app will help the attendance, meaning better funding for that school district.
- **Persona 4**: Teachers in the Gotham city school district will have full hands on the teacher app to track students attendance , once a student doesn’t show up it will ping the students’ parents.

## Product Scenarios

### Product Scenario 1

**ACME Bank** has recently onboarded a new business line which will introduce new customers from the European Union. The new portfolio of customers includes clients known to receive and send funds transfers from or to cryptocurrency exchanges, including decentralized exchanges. The new customers expose the bank to potential risk associated with the origin of the funds. **Rick James**, head of Financial Crime Compliance, gathers the compliance team to assess the risk associated with the new customers. Promptly, the compliance data management team collects the wallet addresses associated with these onboard clients, to load them into Blockr.io. Within minutes, Rick James is notified of risky transactions and the alerts are routed to the investigations team.

**Kathy Griffin**, Head of Sanctions screening, was tasked with assessing the risk associated with ACME Bank’s newly onboarded clients. Kathy assembles her investigations team to review the exceptions identified by Blockr.io. Kathy understands how important this assignment is, so she utilizes Blockr.io's real-time dashboard to monitor the progress her team is making as they review exceptions, and credible concerns are identified.

**Elis Jones** is a 15 year old Sophomore at Gotham High School. He is the child of single mother Eliza Jones. His mother works double shift throughout the week so she is not able to be as active in Elis education as he would like. On average Elis misses 11 of the 30 class periods scheduled per week. His mother is not even in the know on this situation. By using teacher.io Elis’ mother will be notified as to when he is missing class so she can take action with her son. Elis has been taking advantage of the freedom afforded from his mother’s work schedule.

## User Stories

### Feature1: Text Notification

**Description**

- As a Blockr.io client, I need a way to manage my Blockr.io subscriptions which include adding and removing users.
- As an investigator using Blockr.io, I need a way to log into the application. Authentication will grant me the necessary permission to complete my tasks.
- As a member of the organization's (client) leadership team, I need to log into the Blockr.io application and access dashboards.

**Constraints**

Authentication from the SaaS application requires verification through the client’s authentication protocol or through our authentication mechanism.

**Comments**

- All users will authenticate through a single page and will be routed to the appropriate instance based on access policies setup by instance administrators.
- Users may only set up an account through invitation from instance administrators.

### Feature2: Student Database

**Description**

- As a Blockr.io user, I want to visualize my organization’s performance and usage of the Blockr.io application.
- As a Blockr.io user, I need to know the breakdown of exception backlogs, displayed by status group (open/in-progress/closed).
- As a Blockr.io user, I need to know if exceptions were assigned to me for further review.
- As a Blockr.io user, I need to know when progress was made on an exception I am "watching".
- As a member of the Leadership/management team, I want to know how many active users are working.
- As a member of the Leadership/management team, I want to know how many exceptions were escalated for further review by the investigations team.

**Constraints**

Dashboard must only share tenant-specific statistics.

### Feature3: Teacher Friendly User Interface

**Description**

- As an investigator, I need a way to search a given bitcoin address on the blockchain.
- As an investigator, I need a way to view connections to a bitcoin address as a graph.
- As an investigator, I need a way to click on a bitcoin address node on the graph and read information about the address such as the number of transactions, holdings, and reports of abuse.
- As an investigator, I need a way to flag bitcoin address nodes for ongoing monitoring.
- As an investigator, I need a way to assign a network graph to a colleague, including escalating to senior management.
- As an investigator, I need a way to enter comments about a network to share with colleagues, including senior management.

**Constraints**

Sharing/assigning networks to colleagues is limited to those within the tenant instance.

### Feature4: Tracking System for Student Truancy

**Description**

- As an administrator, I need to have a way to invite users to the organization’s instance.
- As an administrator, I need a way to manage a watchlist of addresses.
- As an administrator, I need a way to adjust the parameters for our transactions monitoring system.

**Constraints**

Limited to the tenant's instance.

## User Experience

Describe the user interface for your product.

- [Insert simple wireframes of your product—what will it look like from a user interface perspective]

  Teacher arrives at homepage: <insert picture here>

  Teachers are prompted to sign in: <insert picture here>

  Gain access to take student attendance: <insert picture here>

  Click the class they are teaching during that period: <insert picture here>

  In case student is skipping teacher marks the student as skipping : <insert picture here>

  Notification is sent to the parent : <insert picture here>

  Teacher can then logout or return to their main page: <insert picture here>
