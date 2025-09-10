## Odoo Employee Leave Management System 🌟

A custom Odoo 18 module designed to streamline employee leave requests, approvals, and management. This system provides a user-friendly interface for employees to submit leave requests and for managers to efficiently review and act upon them, all within the Odoo ecosystem.

### 🚀 Features

  * **Leave Request Submission**: Employees can easily submit new leave requests, specifying the leave type, start date, end date, and reason.
  * **Leave Type Management**: Administrators can define and manage various leave types (e.g., Annual Leave, Sick Leave, Unpaid Leave) with configurable annual limits.
  * **Automated Workflow**: The system supports a clear workflow: Draft -\> To Approve -\> Approved/Refused.
  * **Managerial Approval**: Requests are routed to the employee's manager for review and approval/rejection.
  * **Status Tracking**: Real-time status updates for leave requests, visible to both employees and managers.
  * **Leave Balances (Optional Enhancement)**: Potential to integrate with leave balance tracking for employees.
  * **Notifications**: In-app notifications for new requests, approvals, and rejections (can be extended to email notifications).
  * **Calendar View**: Visualize approved leave requests on a calendar for better team planning.
  * **Security Rules**: Granular access control ensuring employees see only their requests, while managers see their team's requests.

### 🛠️ Technologies Used

  * **Odoo Version**: 18.0
  * **Backend**: Python
  * **Frontend**: XML, QWeb, JavaScript (OWL for advanced views if implemented)
  * **Database**: PostgreSQL

### 📂 Module Structure

The module `my_leave_management` is structured according to Odoo best practices:

```
my_leave_management/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── leave_request.py
│   └── leave_type.py
├── views/
│   ├── leave_request_views.xml
│   ├── leave_type_views.xml
│   └── leave_menu.xml
├── security/
│   ├── ir.model.access.csv
│   └── ir.rule.xml
└── data/
    └── leave_sequence.xml
```

### 💡 Core Models

  * **`my.leave.type`**: Manages different categories of leave (e.g., Annual, Sick).
      * `name`: Name of the leave type.
      * `limit`: Annual days entitlement.
  * **`my.leave.request`**: Stores individual leave requests.
      * `employee_id`: The employee submitting the request.
      * `leave_type_id`: The type of leave requested.
      * `start_date`, `end_date`: Duration of the leave.
      * `number_of_days`: Computed duration.
      * `state`: Current status (draft, to\_approve, approved, refused).
      * `reason`: Employee's reason for leave.
      * `manager_id`: The employee's direct manager (related field).

### 🚀 Installation

1.  Clone this repository into your Odoo custom addons path.
2.  Restart your Odoo server.
3.  Navigate to the Apps menu, update the apps list, and search for "My Leave Management".
4.  Click "Install".

### 📚 Usage

1.  **Configuration**:
      * Go to **My Leaves \> Configuration \> Leave Types** to define your leave policies.
2.  **Employee**:
      * Navigate to **My Leaves \> My Requests** to submit a new leave request.
      * Track the status of your submitted requests.
3.  **Manager**:
      * Navigate to **My Leaves \> Requests to Approve** to see pending requests from your team.
      * Approve or refuse requests.

### 📝 Further Enhancements (Future Scope)

  * **Leave Balance Tracking**: Implement tracking of remaining leave days per employee and leave type.
  * **Automated Deductions**: Automatically deduct approved leave days from employee balances.
  * **Public Holiday Integration**: Consider holidays when calculating leave days.
  * **Email Notifications**: Implement email alerts for request status changes.
  * **Reporting**: Develop custom reports for leave analysis.
