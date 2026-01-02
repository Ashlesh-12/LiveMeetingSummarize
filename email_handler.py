"""
Email Handler - Sends real emails with proper configuration
Supports Gmail, Outlook, and custom SMTP servers
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import streamlit as st
from datetime import datetime
import json
import base64

class EmailHandler:
    def __init__(self, smtp_host, smtp_port, sender_email, sender_password):
        """
        Initialize email handler
        
        Args:
            smtp_host: SMTP server address (e.g., smtp.gmail.com)
            smtp_port: SMTP port (usually 587 for TLS, 465 for SSL)
            sender_email: Sender email address
            sender_password: Sender password or app-specific password
        """
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
    
    def send_summary_email(self, recipient_email, subject, summary_text, segments, transcript):
        """
        Send summary email with transcript
        
        Args:
            recipient_email: Recipient email address
            subject: Email subject
            summary_text: Summary content
            segments: List of transcript segments
            transcript: Full transcript
            
        Returns:
            tuple: (success: bool, message: str)
        """
        try:
            # Validate email
            if not self._validate_email(recipient_email):
                return False, "❌ Invalid email address"
            
            if not self.sender_email or not self.sender_password:
                return False, "❌ Email credentials not configured. Set in Settings sidebar."
            
            # Create message
            msg = MIMEMultipart("alternative")
            msg["Subject"] = subject
            msg["From"] = self.sender_email
            msg["To"] = recipient_email
            
            # Create HTML body
            html_body = self._create_html_email(subject, summary_text, segments, transcript)
            
            # Attach HTML
            html_part = MIMEText(html_body, "html")
            msg.attach(html_part)
            
            # Send email
            try:
                # Try SSL first (port 465)
                if self.smtp_port == 465:
                    server = smtplib.SMTP_SSL(self.smtp_host, self.smtp_port, timeout=10)
                else:
                    # TLS (port 587)
                    server = smtplib.SMTP(self.smtp_host, self.smtp_port, timeout=10)
                    server.starttls()
                
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
                server.quit()
                
                return True, f"✅ Email sent successfully to {recipient_email}"
                
            except smtplib.SMTPAuthenticationError:
                return False, "❌ Authentication failed. Check email and password."
            except smtplib.SMTPException as e:
                return False, f"❌ SMTP Error: {str(e)}"
            except Exception as e:
                return False, f"❌ Connection Error: {str(e)}"
                
        except Exception as e:
            return False, f"❌ Error: {str(e)}"
    
    @staticmethod
    def _validate_email(email):
        """Validate email format"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def _create_html_email(subject, summary_text, segments, transcript):
        """Create HTML email body"""
        
        speakers = list(set(seg['speaker'] for seg in segments))
        
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #333; line-height: 1.6; }}
                .container {{ max-width: 800px; margin: 0 auto; padding: 20px; background: #f5f5f5; }}
                .header {{ background: linear-gradient(135deg, #FF6B6B 0%, #FF8E8E 100%); color: white; padding: 20px; border-radius: 8px; text-align: center; }}
                .header h1 {{ margin: 0; font-size: 28px; }}
                .header p {{ margin: 5px 0 0 0; font-size: 14px; opacity: 0.9; }}
                .section {{ background: white; margin: 20px 0; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
                .section h2 {{ color: #FF6B6B; border-bottom: 2px solid #FF6B6B; padding-bottom: 10px; }}
                .summary {{ background: #fff3e0; padding: 15px; border-left: 4px solid #FF6B6B; border-radius: 4px; }}
                .speakers {{ display: flex; gap: 10px; flex-wrap: wrap; }}
                .speaker-badge {{ background: #FF6B6B; color: white; padding: 8px 12px; border-radius: 20px; font-size: 12px; }}
                .transcript {{ background: #f9f9f9; padding: 15px; border-radius: 4px; max-height: 300px; overflow-y: auto; }}
                .segment {{ margin: 10px 0; padding: 10px; border-left: 3px solid #FF6B6B; }}
                .speaker-name {{ color: #FF6B6B; font-weight: bold; }}
                .time {{ color: #999; font-size: 12px; }}
                .footer {{ text-align: center; color: #999; font-size: 12px; margin-top: 20px; padding-top: 20px; border-top: 1px solid #eee; }}
                .action-button {{ display: inline-block; background: #FF6B6B; color: white; padding: 12px 30px; text-decoration: none; border-radius: 4px; margin: 10px 0; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>🎤 Meeting Summary Report</h1>
                    <p>{datetime.now().strftime('%B %d, %Y at %H:%M')}</p>
                </div>
                
                <div class="section">
                    <h2>📋 Summary</h2>
                    <div class="summary">
                        {summary_text.replace(chr(10), '<br>')}
                    </div>
                </div>
                
                <div class="section">
                    <h2>👥 Speakers</h2>
                    <div class="speakers">
                        {''.join(f'<span class="speaker-badge">{speaker}</span>' for speaker in speakers)}
                    </div>
                </div>
                
                <div class="section">
                    <h2>📝 Transcript</h2>
                    <div class="transcript">
                        {''.join(f'''
                        <div class="segment">
                            <span class="speaker-name">{seg.get('speaker', 'Unknown')}</span>
                            <span class="time">({seg.get('start', '0:00')} - {seg.get('end', '0:00')})</span>
                            <p>{seg.get('text', '')}</p>
                        </div>
                        ''' for seg in segments[:10])}  <!-- Limit to first 10 segments -->
                    </div>
                </div>
                
                <div class="footer">
                    <p>Generated by Live Meeting Summarizer | Powered by Streamlit & AI</p>
                    <p>📧 For questions or support, please contact us.</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        return html
