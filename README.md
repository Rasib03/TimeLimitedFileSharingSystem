CloudDrive — Time-Limited File Sharing System
A Django-based file management and sharing platform built for controlled, time-bound document distribution between an admin (master user) and their clients.

Overview
CloudDrive is a private file sharing system where a single master administrator uploads and shares files with registered client accounts. Every shared file carries an expiry timestamp — once the window closes, the file automatically switches to view-only mode, giving the master full control over how long clients can interact with content.

Key Features
File Management The master can upload Excel (.xlsx), Word (.docx), PDF, and other file types, organizing them into a nested folder structure. Files can be kept private (only for the master) or shared with one or more clients at upload time. Each file is assigned an expiry date and time, after which editing is locked.

Inline Excel Editing Excel files open directly in the browser using an embedded Luckysheet spreadsheet editor — no downloads required. Both the master and authorized clients can edit cells, apply formatting, and save changes back to the server in real time. Changes are persisted to the original .xlsx file using openpyxl. Expired files become read-only automatically.

PDF & DOCX Viewing PDF files render natively in an embedded viewer. DOCX files are displayed via Google Docs Viewer. All file types support direct download at any time.

Client Management The master can create and delete client accounts from a dedicated management panel. Client passwords are visible and editable directly by the master — if a client needs a password change, the master updates it instantly without any request workflow.

Access Control Role-based access separates master and client views entirely. Clients only see files explicitly shared with them. The master has full visibility over all files, folders, and client accounts.

Tech Stack
Backend: Django 6, Python, openpyxl
Frontend: Bootstrap 5, Luckysheet, Bootstrap Icons
Database: SQLite (easily swappable)
Storage: Local media storage via Django's FileField
