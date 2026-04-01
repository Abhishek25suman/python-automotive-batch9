import qrcode

# Complete project content for QR code
qr_data = """Automotive Testing Batch-9 - Group 1 PROJECT REPORT

 SUBJECT: Embedded Systems & Automotive Software Testing

 TEAM MEMBERS & PERFORMANCE:
• Abhishek     | 95/100 | A+ |  Developer
• Lokesh       | 92/100 | A  | Test Automation
• Ritikesh     | 96/100 | A+ | Hardware Integration  
• Sudha        | 94/100 | A+ | CAN Protocol Testing
• Yamini       | 97/100 | A+ | HMI Development
• Pavithra     | 91/100 | A  | Documentation

 TEAM STATS:
Total Marks: 565/600 (94.2%)
Highest: Yamini (97%)
Subject Average: 94.2%

 PROJECT SCOPE:
 ECU Firmware Testing
 CAN Bus Communication
 Infotainment HMI Validation
 Real-time Diagnostics
 Error Code Analysis

SUBMISSION: Jan 2026
 STATUS: COMPLETED """

# Create QR code
qr = qrcode.QRCode(
    version=4,  
    error_correction=qrcode.constants.ERROR_CORRECT_H,  
    box_size=12,
    border=5
)

qr.add_data(qr_data)
qr.make(fit=True)


qr_img = qr.make_image(fill_color="blue", back_color="white")


qr_img.save("Project_report_qrcode.png")

print(" Complete Project QR generated!")