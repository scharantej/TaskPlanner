## Flask Application Design

**HTML Files**

- **index.html:** The main page of the application. It should include a form for users to input their tasks and time slots.
- **planner.html:** The page that displays the user's scheduled tasks and time slots.

**Routes**

- **root:** The route for the main page. It should render the **index.html** file.
- **schedule:** The route that handles the user's input and creates the schedule. It should receive the user's tasks and time slots as form data and render the **planner.html** file with the generated schedule.