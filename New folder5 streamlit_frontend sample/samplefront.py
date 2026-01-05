import streamlit as st
import time
from datetime import datetime
import json

# Page config
st.set_page_config(
page_title="Live Meeting Summarizer",
page_icon="",
layout="wide"
)

#Initialize session state

if 'is_recording' not in st.session_state:
    st.session_state.is_recording = False
if 'transcript' not in st.session_state:
    st.session_state.transcript = []
if 'summary' not in st.session_state:
    st.session_state.summary = ""
if 'key_points' not in st.session_state:
    st.session_state.key_points = []
if 'action_items' not in st.session_state:
    st.session_state.action_items = []

#Title and header
st.title(" Live Meeting Summarizer")
st.markdown("Real-time transcription and intelligent meeting summarization")

#Sidebar for controls
with st.sidebar:
    st.header("Meeting Controls")
    

#Recording controls
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Start", disabled=st.session_state.is_recording, use_container_width=True):
            st.session_state.is_recording = True
            st.rerun()
        
        with col2:
            if st.button("Stop", disabled=not st.session_state.is_recording, use_container_width=True):
                st.session_state.is_recording = False
                st.rerun()

        if st.button("Clear", use_container_width=True):
            st.session_state.transcript = []
            st.session_state.summary = ""
            st.session_state.key_points = []
            st.session_state.action_items = []
            st.rerun()  

st.divider()

#Meeting info
st.subheader("Meeting Info") 
meeting_title = st.text_input("Meeting Title", "Team Standup") 
participants = st.text_area("Participants", "John, Sarah, Mike")

st.divider()

#Settings
st.subheader("Settings")
summarize_interval = st.slider("Auto-summarize every (seconds)", 30, 300, 60) 
language = st.selectbox("Language", ["English", "Spanish", "French", "German", "Chinese"])



#Status indicator

st.divider()
if st.session_state.is_recording:
    st.success(" Recording in progress...")
else:
    st.info(" Not recording")

#Main content area with tabs

tab1, tab2, tab3, tab4 = st.tabs([" Live Transcript", " Summary", "☑ Action Items", "Export"])
with tab1:
    st.subheader("Live Transcription")

    #Transcript display area
    transcript_container = st.container(height=500)
    
    with transcript_container:
        if st.session_state.transcript:
            for entry in st.session_state.transcript:
                timestamp = entry.get('timestamp','')
                speaker = entry.get('speaker', 'Unknown')
                text = entry.get('text','')
            
                col1, col2 = st.columns([1, 5]) 
                with col1:
                    st.caption(f"**{speaker}**")
                    st.caption(timestamp)
                with col2:
                    st.write(text)
                st.divider()
        else:
            st.info("No transcript available. Start recording to begin transcription.")

    #Simulate live transcription (replace with actual transcription API)

    if st.session_state.is_recording:
        sample_speakers = ["Alice", "Bob", "Charlie"]
        sample_texts = [
"Let's discuss the progress on the new feature.",
"I've completed the backend implementation.",
"The frontend integration is 80% done.",
"We need to address the performance issues.",
"I'll work on the documentation this week.",
"Can we schedule a code review for tomorrow?",
        ]

        #Add new transcript entry (simulated)
        if len(st.session_state.transcript) < 10:
            import random

            new_entry = {
                'timestamp': datetime.now().strftime("%H:%M:%S"),
                'speaker': random.choice(sample_speakers),
                'text': random.choice(sample_texts)
            }
            st.session_state.transcript.append(new_entry)
            st.rerun()      


with tab2:
    st.subheader("Meeting Summary")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.button(" Generate Summary", use_container_width= True):

            #Simulate summary generation (replace with actual Al summarization)
            if st.session_state.transcript:
                with st.spinner("Generating summary..."):
                    time.sleep(2)
                    st.session_state.summary = """ 
**Meeting Overview:**
The team discussed progress on the new feature development. Key accomplishments include backend implementation and frontend integration.

**Main Topics:**
-Backend implementation status
-Frontend integration progress (80% complete)
-Performance optimization needs
-Documentation requirements
-Code review scheduling

**Decisions Made:**
- Schedule code review for tomorrow
- Prioritize performance issue resolution
- Assign documentation tasks for this week
"""

                    st.session_state.key_points = [

                        "Backend implementation completed",
                        "Frontend integration 80% done",
                        "Performance issues identified",
                        "Code review scheduled for tomorrow",
                        "Documentation work assigned"
                    ]

                st.success("Summary generated successfully!")
                st.rerun()

    if st.session_state.summary:
        st.markdown(st.session_state.summary)

        st.subheader("Key Points")
        for i, point in enumerate(st.session_state.key_points, 1):
            st.markdown(f"({i}). {point}")

    else:
        st.info("Generate a summary to see the meeting overview and key points.")

with tab3:
    st.subheader("Action Items")

    if st.button("Extract Action Items", use_container_width=False):

        #Simulate action item extraction (replace with actual Al extraction)

        if st.session_state.transcript:

            with st.spinner("Extracting action items..."):

                time.sleep(1.5)
                st.session_state.action_items = [
                    {"task": "Complete frontend integration", "assignee": "Bob", "deadline": "This week"},
                    {"task": "Address performance issues", "assignee": "Charlie", "deadline": "Next sprint"},
                    {"task": "Write documentation", "assignee": "Alice", "deadline": "This week"},
                    {"task": "Conduct code review", "assignee": "Team", "deadline": "Tomorrow"},
                ]

            st.success("Action items extracted!")
            st.rerun()

    if st.session_state.action_items:
        for i, item in enumerate(st.session_state.action_items, 1): 
            with st.expander (f"Action Item (i): (item['task']]", expanded=True):

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**Assignee:** {item['assignee']}") 
                with col2:
                    st.write(f"**Deadline:** {item['deadline']}")
                with col3:
                    st.checkbox("Completed", key=f"action_{i}")
    else:
        st.info("Extract action items to see tasks and assignments from the meeting.")

with tab4:
    st.subheader("Export Meeting Data")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button(" Export as Text", use_container_width=True):
            export_text = f"Meeting Title: {meeting_title}\n"
            export_text += f"Date: {datetime.now().strftime('%Y-%m-%d')}\n"
            export_text += f"Participants: {participants}\n\n"
            export_text += "TRANSCRIPT\n"

            for entry in st.session_state.transcript:
                export_text += f"[{entry['timestamp']}] {entry['speaker']}: {entry['text']}\n"
            export_text += f"\nSUMMARY\n{st.session_state.summary}\n"
           
            st.download_button(
                label="Download Text File",
                data=export_text,
                file_name=f"meeting_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain"
            )

    with col2:
        if st.button("Export as 3500", use_container_width=True):
            export_data = {
                "meeting title": meeting_title,
                "date": datetime.now().strftime('%Y-%m-%d %H:%M'),
                "participants": participants,
                "transcript": st.session_state.transcript,
                "summary": st.session_state.summary,
                "key points": st.session_state.key_points,
                "action items": st.session_state.action_items
            }

            st.download_button(
                label="Download JSON File",
                data=json.dumps(export_data, indent=2),
                file_name=f"meeting_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )
            
    with col3:
        if st.button(" Email Summary", use_container_width=True): st.info("Email functionality would be implemented here with SMTP integration.")

st.divider()
st.caption("Live Meeting Summarizer v1.0 | Powered")  #to run in streamlit 1st- pip install streamlit and 2nd-streamlit run app.py

