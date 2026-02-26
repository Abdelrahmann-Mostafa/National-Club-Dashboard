# National Club Dashboard Project

This repository contains a visualization dashboard that presents data about national club membership. The project was developed as part of a visualization course and includes both a web application and a Jupyter notebook for analysis.

## Structure

```
README.md
names.csv
dashboard.html
National_Club_Dashboard_Fixed.ipynb
NationalClubDashboard/
    app.py
    club_data.csv
    generate_data.py
    requirements.txt
    templates/
        index.html
```

- **app.py**: Flask application to serve the dashboard.
- **generate_data.py**: Script for generating or updating club data CSV.
- **club_data.csv**: Sample data used by the app.
- **names.csv**: Additional dataset with names referenced in analysis.
- **dashboard.html**: Static HTML export of the dashboard.
- **National_Club_Dashboard_Fixed.ipynb**: Jupyter notebook containing analysis and visualization code.

## Requirements

Dependencies for the Flask app are listed in `NationalClubDashboard/requirements.txt`.

```text
flask
pandas
```

Install with:

```sh
python -m pip install -r NationalClubDashboard/requirements.txt
```

## Running the Application

1. Ensure dependencies are installed.
2. From the project root, start the Flask server:

   ```sh
   cd NationalClubDashboard
   python app.py
   ```

3. Open a browser and navigate to `http://localhost:5000` to view the dashboard.

## Notebook

The Jupyter notebook `National_Club_Dashboard_Fixed.ipynb` contains exploratory analysis and can be run with:

```sh
jupyter notebook National_Club_Dashboard_Fixed.ipynb
```

## Data

- `club_data.csv` holds the club membership data used by the dashboard.
- `names.csv` includes additional information used in the notebook.

## License

This project is for educational purposes.
