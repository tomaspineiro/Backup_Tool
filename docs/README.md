# Backup Tool

Backup Tool is a Python application designed to automate the backup process of Cisco switches and routers. It provides a user-friendly interface for entering device information and managing backup configurations.

## Features

- **Automated Backups**: The tool allows you to easily schedule and perform automated backups of Cisco devices.
- **Multiplatform**: The application is developed as a desktop application and is compatible with both Windows and Linux operating systems.
- **User Interface**: Backup Tool utilizes the Tkinter library to create a graphical user interface, making it intuitive and easy to use.
- **Configuration Management**: You can modify, delete, and manage backup configurations through the user interface.
- **Secure Credentials**: The application securely stores user credentials in the "credentials.json" file, ensuring the protection of sensitive information.

## Folder Structure

The following is the suggested folder structure for the Backup Tool project:

```
backup_tool/
├── app/
│   ├── __init__.py
│   ├── backup.py
│   └── ui.py
├── tests/
│   ├── __init__.py
│   └── test_backup.py
├── config/
│   └── __init__.py
├── credentials/
│   └── credentials.json
├── templates/
│   └── main_template.ui
├── docs/
│   └── README.md
├── requirements.txt
└── main.py
```

## Installation

1. Clone the Backup Tool repository:

```
git clone https://github.com/tomaspineiro/Backup_Tool
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Run the application:

```
python main.py
```

2. Enter the necessary device information in the user interface.
3. Configure the backup settings and schedule as desired.
4. Click on the "Start Backup" button to initiate the backup process.

For detailed instructions and additional information, please refer to the [User Guide](docs/user_guide.md).

## Contributing

Contributions to the Backup Tool project are welcome! If you would like to contribute, please follow the guidelines outlined in [CONTRIBUTING.md](docs/CONTRIBUTING.md).

## License

Backup Tool is released under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions regarding Backup Tool, please contact us at backuptool@example.com.

We appreciate your interest in the project and look forward to your valuable contributions!

