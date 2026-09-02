# CycloRoute

**CycloRoute** is an intelligent desktop application for cyclist-specific route analysis and recommendation.

The project combines **Physics, Mathematics, Python, data analysis, geographic data, weather data, databases, testing, and potentially machine learning** to evaluate cycling routes more meaningfully than ordinary navigation systems.

---

## Project Goals

CycloRoute is intended to allow a user to mainly provide:

- Start location
- Destination

The application will then obtain and process available geographic and environmental information, such as:

- Route geometry
- Elevation
- Road gradient
- Wind speed and direction
- Temperature
- Humidity
- Rainfall / precipitation
- Weather forecasts
- Other useful environmental information where available

The route will be divided into segments so that different parts of the route can be analyzed separately.

---

## Physics-Based Route Analysis

The project will use physics and mathematics to estimate factors affecting cycling, including:

- Road gradient and slope angle
- Gravitational resistance
- Rolling resistance
- Wind velocity vectors
- Cyclist velocity vectors
- Relative wind velocity
- Relative wind speed
- Relative wind direction
- Other relevant cycling forces where practical

The results can then be combined into route-level comparisons.

The current development already includes basic physics functions for gradient, gravitational resistance, rolling resistance, velocity vectors, and relative wind calculations.

---

## Geographic and Weather Data

CycloRoute is designed around **open and freely accessible data/services wherever practical**.

### Mapping and Routing

The project will use **OpenStreetMap-based geographic data** and suitable open/free routing services or tools.

**Google Maps and Google Maps APIs are not part of the project.**

### Environmental Data

Weather and environmental information may be obtained through suitable APIs or other available data sources.

Because external services can have:

- Rate limits
- Fair-use restrictions
- Attribution requirements
- Incomplete coverage
- Changing availability
- Accuracy limitations

the application will be designed so that external data sources can be replaced or extended when necessary.

---

## Local User Knowledge

Automated geographic and weather services cannot know every local condition, particularly in rural areas.

CycloRoute may therefore allow users to provide useful local information, for example:

- Flood-prone roads
- Waterlogging
- Rain-sensitive road sections
- Poor road surfaces
- Other local hazards or conditions

This information can be stored and considered in future route analysis.

---

## Route Recommendation

The application will compare available routes using the collected geographic, environmental, and physics-based information.

The intended result is an automated recommendation of a suitable route based on factors relevant to cycling.

The recommendation system is not intended to replace real-world judgement or act as a safety guarantee.

---

## Machine Learning

Machine learning is an **optional / experimental part** of the project.

If enough useful data is collected, machine learning may be investigated for tasks such as:

- Route difficulty estimation
- Travel-time estimation
- Environmental-impact estimation
- Improving route recommendations

Machine learning will only be used where there is sufficient data and a meaningful reason to use it.

---

## Desktop GUI

CycloRoute is planned as a professional desktop application.

The GUI is expected to provide features such as:

- Start and destination input
- Map display
- Route comparison
- Environmental information
- Physics calculations
- Graphs and visual analysis
- Route recommendation
- Local-condition information

The project is intended to remain reasonably portable across operating systems.

---

# 🔴 FEDORA / FEDORA-BASED SYSTEMS ONLY

**The commands in the system-installation section below are specifically for Fedora and Fedora-based systems.**

**If you are using Ubuntu, Debian, Arch, openSUSE, Windows, macOS, or another operating system, DO NOT copy these commands directly. Adapt them to your operating system and package manager.**

**The Python project itself is intended to remain portable. This warning applies specifically to the optional system-level setup below.**

---

## Python Environment

For CycloRoute development, Python packages should be installed in the project's **virtual environment (`.venv`) using `pip`**.

Example:

```bash
source .venv/bin/activate
python -m pip install --upgrade pip
```

Then install the required Python dependencies with `pip`.

The exact dependency list will be maintained as the project develops.

Typical project dependencies include:

```text
PySide6
NumPy
SciPy
Pandas
Requests / HTTPX
Matplotlib
Scikit-learn
pytest
```

Python's standard library is also used where appropriate, including modules such as:

```text
math
json
datetime
sqlite3
```

### Important

Do **not** treat the Fedora `dnf` commands as the normal way to install CycloRoute's Python dependencies.

The preferred project-level approach is:

```bash
source .venv/bin/activate
python -m pip install <package>
```

This keeps project dependencies isolated from the system Python installation.

---

## Fedora System Dependencies

Some GUI or native components may require system packages on Fedora/Fedora-based systems.

If a future dependency requires a Fedora system package, install that package separately with `dnf`.

For example, system-level development/runtime dependencies may be installed using:

```bash
sudo dnf upgrade --refresh
sudo dnf install python3 python3-pip python3-devel gcc gcc-c++
```

Additional Fedora packages should only be added when they are actually required by the project's dependency setup.

---

## Development Environment

The project uses:

- Python 3
- PyCharm Community Edition
- PyCharm Toolbox
- Python virtual environment (`.venv`)
- Git
- GitHub
- pytest

The project should be developed and tested in the virtual environment rather than relying on globally installed Python packages.

---

## Testing

Testing is performed with **pytest**.

Physics calculations are tested separately so that individual components can be verified before being combined into larger route-analysis systems.

Examples of currently tested concepts include:

- Zero gradient
- Positive gradient
- Negative gradient
- Gravitational resistance
- Rolling resistance
- Wind/vector calculations

---

## Project Architecture

The project is being developed using modular components.

The general structure is intended to separate responsibilities such as:

```text
cycloroute/
├── physics.py
├── wind.py
├── ...
data/
├── ...
tests/
├── ...
```

Individual modules should perform focused tasks, while higher-level functions coordinate those modules.

This makes the project easier to:

- Test
- Debug
- Extend
- Replace individual data sources
- Add future features

---

## Development Philosophy

CycloRoute is being developed incrementally.

The current priority is to build and verify the **physics and mathematical foundations** before connecting them to larger systems such as:

- Route services
- Elevation data
- Weather APIs
- Databases
- GUI components
- Route comparison
- Machine learning

Features will be added only after their underlying concepts can be tested reliably.

---

## Traffic Data

Traffic data is **not a planned component** of CycloRoute.

The project focuses on cyclist-specific factors such as:

- Gradient
- Elevation
- Wind
- Weather
- Rainfall
- Road conditions
- Physics-based cycling effort

---

## Status

CycloRoute is currently under active development.

The physics foundation includes working implementations for:

- Road gradient
- Gravitational resistance
- Rolling resistance
- Velocity vectors
- Relative velocity
- Relative velocity magnitude
- Relative wind direction

Further development will integrate these calculations with route and environmental data.

---

## License

See the repository's `LICENSE` file for licensing information.
