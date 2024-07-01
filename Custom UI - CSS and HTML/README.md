# Custom UI - CSS and HTML

Discover our Custom UI showcase app for Streamlit! 🎨✨

Custom UI enables customization of the look, feel, and front-end behavior of Streamlit in Snowflake apps.
This feature supports the following:

- Custom HTML and CSS using `unsafe_allow_html=True` in [st.markdown](https://docs.streamlit.io/library/api-reference/text/st.markdown).
- Iframed HTML, CSS, and JavaScript using [st.components.v1.html](https://docs.streamlit.io/develop/api-reference/custom-components/st.components.v1.html).

This app demonstrates how you can transform the default Streamlit interface by applying custom styles to various elements such as buttons, text, and containers. By leveraging CSS, the app provides a more personalized experience, illustrating the flexibility and aesthetic potential of combining Streamlit's interactive features with custom styling.

👉 Make sure to also check out the "Custom UI Features" mode for more examples of what's possible, and source code to get started.

**Custom UI for Streamlit in Snowflake is currently in Public Preview.
[Read the docs to learn more.](https://docs.snowflake.com/en/developer-guide/streamlit/additional-features#custom-ui-in-sis)**

<img src="./assets/custom_ui_app.gif" width="600" />

## Installation

1. Open a new SQL Worksheet.

2. Copy the contents of the file `data/creation_script.sql` into the Worksheet. Execute the `CREATE` statements of the script, which creates a database and schema.

3. When you create a new Streamlit App, Snowflake automatically generates a new stage for this app. Access this stage in the Data section on the left side of the screen. Navigate to Databases, find the database associated with your Streamlit App (e.g., `SAMPLEDATABASE.CUSTOM_UI`).

![Create Streamlit App](../instructions_assets/streamlit_app.png)

![Left Menu](../instructions_assets/left_menu.png)

4. Select the database, then choose the schema where you created the Streamlit App (e.g., public).

![Look for database](../instructions_assets/look_for_database.png).

5. Navigate to Stages to view the available stages. Snowflake has automatically created a Stage with an autogenerated name.

![Look for database](../instructions_assets/look_for_database2.png).

6. Click on the stage name. The first time, it will prompt you to “Enable Directory Listing”. Click on that button.

![Enable Directory](../instructions_assets/enable_directory.png).

7. Choose a warehouse.

![Select warehouse](../instructions_assets/select_warehouse.png).

8. Click on “+ Files” in the upper right corner to open a popup where you can add the required files.

9. Upload the files by clicking on the "Upload" button in the lower right corner. Note that if a file has the same name as an existing file in the stage, the new file will overwrite the previous one (Select all the files in the root of the folder).

![Select files](../instructions_assets/upload_file.png).

10. With these steps, you have successfully uploaded files into your Streamlit App.