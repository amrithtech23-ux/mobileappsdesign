<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mobile App Forge | Bold Frame Studio</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background: #0a121c; font-family: 'Inter', system-ui, sans-serif; padding: 2rem 1.8rem; color: #eef4ff; }
        .app-container { max-width: 1600px; margin: 0 auto; background: #101a26; border: 3px solid #2d4a6e; border-radius: 2rem; box-shadow: 0 20px 35px -10px rgba(0,0,0,0.5); overflow: hidden; }
        .inner-wrap { padding: 2rem 2rem 2.2rem 2rem; }
        .hero { text-align: center; margin-bottom: 2.5rem; border-bottom: 3px solid #2e577a; padding-bottom: 1.5rem; }
        .hero h1 { font-size: 2.4rem; font-weight: 800; background: linear-gradient(135deg, #fff, #7ab3c8); -webkit-background-clip: text; background-clip: text; color: transparent; display: inline-flex; align-items: center; gap: 14px; }
        .hero h1 span { background: #1e3a5f; border: 1.5px solid #4d7ca1; border-radius: 60px; padding: 0.2rem 1rem; font-size: 0.85rem; color: #cbe5fe; font-weight: 600; }
        .sub { color: #9bb7d0; margin-top: 0.7rem; font-weight: 500; font-size: 1rem; }
        .dashboard { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin: 2rem 0; }
        .control-panel { background: #0f1822; border: 2.5px solid #2e577a; border-radius: 1.5rem; padding: 1.6rem 1.8rem; }
        .result-panel { display: flex; flex-direction: column; gap: 1.8rem; }
        .form-group { margin-bottom: 1.8rem; }
        label { font-weight: 700; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; color: #c2dcf5; display: block; margin-bottom: 0.6rem; border-left: 3px solid #3b82f6; padding-left: 10px; }
        select, button { width: 100%; padding: 0.9rem 1rem; border-radius: 1rem; border: 2px solid #2d4f70; background: #0e1722; font-size: 0.95rem; font-weight: 500; color: #f0f6fe; transition: all 0.2s; cursor: pointer; font-family: inherit; }
        select:focus, button:focus { outline: none; border-color: #60a5fa; box-shadow: 0 0 0 3px rgba(96,165,250,0.3); }
        button { background: #1a334c; color: white; border: 2px solid #3e6d91; font-weight: 700; margin-top: 0.5rem; display: flex; align-items: center; justify-content: center; gap: 0.6rem; transition: 0.15s; }
        button:hover { background: #234b6e; border-color: #5f9dc9; transform: translateY(-1px); }
        .reset-btn { background: #111e2c; color: #bfd9f0; border: 2px solid #3f5c78; }
        .button-group { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 0.5rem; }
        .ux-card, .ui-card { background: #0b131e; border: 3px solid #2d577b; border-radius: 1.5rem; box-shadow: 0 12px 20px -8px rgba(0,0,0,0.5); overflow: hidden; }
        .card-header { background: #11212f; padding: 1rem 1.5rem; border-bottom: 3px solid #2d577b; font-weight: 800; font-size: 1.25rem; display: flex; align-items: center; gap: 12px; color: #d9ecff; }
        textarea { width: 100%; padding: 1.3rem; border: none; font-family: 'SF Mono', monospace; font-size: 0.9rem; line-height: 1.55; color: #eef3fc; background: #0a111b; resize: vertical; min-height: 200px; outline: none; }
        .preview-container { margin-top: 2rem; background: #0b131e; border: 3px solid #2d577b; border-radius: 1.5rem; overflow: hidden; display: none; position: relative; }
        .preview-frame { width: 100%; height: 700px; background: #fff; border: none; }
        .loading-overlay { position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(10, 18, 28, 0.95); display: flex; align-items: center; justify-content: center; flex-direction: column; z-index: 10; display: none; }
        .spinner { width: 50px; height: 50px; border: 4px solid #2d577b; border-top: 4px solid #38bdf8; border-radius: 50%; animation: spin 1s linear infinite; margin-bottom: 1rem; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        footer { text-align: center; font-size: 0.75rem; color: #6d8eb0; border-top: 2px solid #1e3852; padding-top: 1.6rem; margin-top: 0.8rem; font-weight: 500; }
        @media (max-width: 968px) { .dashboard { grid-template-columns: 1fr; } .button-group { grid-template-columns: 1fr; } }
    </style>
</head>
<body>
<div class="app-container">
    <div class="inner-wrap">
        <div class="hero">
            <h1>📱 MOBILE APPs DESIGNS <span>COMPLETE EDITION</span></h1>
            <div class="sub">⚡ 25+ App Types | Dynamic Categories | AI-Powered Generation</div>
        </div>

        <div class="dashboard">
            <!-- LEFT: CONTROLS -->
            <div class="control-panel">
                <div class="form-group">
                    <label>📌 1. MOBILE APPLICATION TYPE</label>
                    <select id="appTypeSelect">
                        <option value="">-- Select Application Type --</option>
                        <option value="E-Commerce & Shopping">🛍️ E-Commerce & Shopping</option>
                        <option value="Healthcare & Telemedicine (Doctors)">🏥 Healthcare & Telemedicine</option>
                        <option value="Personal Assistants & Productivity">🤖 Personal Assistants & Productivity</option>
                        <option value="Transportation & Travel (Bus Reservation)">🚌 Transportation & Travel</option>
                        <option value="Food & Restaurant">🍔 Food & Restaurant</option>
                        <option value="Finance & Banking (FinTech)">💰 Finance & Banking</option>
                        <option value="Social Media & Communication">💬 Social Media & Communication</option>
                        <option value="News, Information & Education">📰 News, Information & Education</option>
                        <option value="Entertainment & Streaming">🎬 Entertainment & Streaming</option>
                        <option value="Utilities & Tools">🔧 Utilities & Tools</option>
                        <option value="Home & Lifestyle Management">🏠 Home & Lifestyle Management</option>
                        <option value="Fitness, Health & Wellness">💪 Fitness, Health & Wellness</option>
                        <option value="Travel & Accommodation">✈️ Travel & Accommodation</option>
                        <option value="Dating & Relationships">💘 Dating & Relationships</option>
                        <option value="Career, Job Search & Freelancing">💼 Career, Job Search & Freelancing</option>
                        <option value="Photography & Video Editing">📸 Photography & Video Editing</option>
                        <option value="Music & Audio Production">🎵 Music & Audio Production</option>
                        <option value="Real Estate & Property">🏡 Real Estate & Property</option>
                        <option value="Automotive & Vehicles">🚗 Automotive & Vehicles</option>
                        <option value="Parenting & Childcare">👶 Parenting & Childcare</option>
                        <option value="Sports & Outdoor Activities">⚽ Sports & Outdoor Activities</option>
                        <option value="AR & VR">🥽 AR & VR</option>
                        <option value="Government & Civic Services">🏛️ Government & Civic Services</option>
                        <option value="Messaging & Communication (Expanded)">📨 Messaging & Communication</option>
                        <option value="Food & Restaurant (Bonus Expanded)">🍽️ Food & Restaurant (Bonus)</option>
                    </select>
                </div>

                <div class="form-group">
                    <label>📂 2. CATEGORY (DYNAMIC)</label>
                    <select id="categorySelect"><option value="">-- First select an App Type --</option></select>
                </div>

                <div class="form-group">
                    <label id="uiScreensLabel">🎨 WAITING FOR SELECTION</label>
                    <select id="uiScreensSelect" disabled><option value="">-- Select App Type and Category first --</option></select>
                </div>

                <div class="button-group">
                    <button id="generateBtn">✨ GENERATE UX & UI</button>
                    <button id="resetBtn" class="reset-btn">⟳ RESET FIELDS</button>
                </div>
                <div class="button-group">
                    <button id="generateWireframeBtn">✨ GENERATE WIREFRAME</button>
                    <button id="generateAngularBtn">✨ GENERATE ANGULAR FRAME</button>
                </div>
            </div>

            <!-- RIGHT: OUTPUTS -->
            <div class="result-panel">
                <div class="ux-card">
                    <div class="card-header"><span>🧠</span> UX PROCESS (USER JOURNEY)</div>
                    <textarea id="uxTextArea" readonly placeholder="User journey will appear here..."></textarea>
                </div>
                <div class="ui-card">
                    <div class="card-header"><span>🎨</span> UI DESIGN (SCREENS & LAYOUTS)</div>
                    <textarea id="uiTextArea" readonly placeholder="UI screens will appear here..."></textarea>
                </div>
            </div>
        </div>

        <div class="result-panel" style="margin-top: 1rem;">
            <div class="ux-card">
                <div class="card-header"><span>🧠</span> WIREFRAME DIAGRAM</div>
                <textarea id="wireframeTextArea" readonly placeholder="Wireframe will appear here..."></textarea>
            </div>
            <div class="ux-card">
                <div class="card-header"><span>🎨</span> ANGULAR FRAME CODE</div>
                <textarea id="angularTextArea" readonly placeholder="Complete HTML code will appear here..."></textarea>
            </div>
        </div>

        <!-- WEB VIEWER -->
        <div class="preview-container" id="previewContainer">
            <div id="loadingOverlay" class="loading-overlay">
                <div class="spinner"></div>
                <div style="color: #eef4ff; font-weight: 600; font-size: 1.2rem;">🤖 Qwen AI is generating code...</div>
            </div>
            <div class="card-header" style="justify-content: space-between;">
                <span>🖥️ WEB VIEWER - LIVE PREVIEW</span>
                <div style="display: flex; gap: 5px;">
                    <button onclick="setPreviewWidth('375px')" style="width: auto; padding: 5px 10px; font-size: 0.8rem;">📱 Mobile</button>
                    <button onclick="setPreviewWidth('768px')" style="width: auto; padding: 5px 10px; font-size: 0.8rem;">📱 Tablet</button>
                    <button onclick="setPreviewWidth('100%')" style="width: auto; padding: 5px 10px; font-size: 0.8rem;">💻 Desktop</button>
                </div>
            </div>
            <iframe id="previewFrame" class="preview-frame" style="width: 375px; margin: 0 auto; display: block;"></iframe>
        </div>
        
        <footer>🧱 BOLD BORDER EDITION | 25+ App Types | Powered by Qwen AI</footer>
    </div>
</div>

<script>
// ==========================================
// COMPLETE CATEGORY MAPPING - ALL 25+ APP TYPES
// ==========================================
const categoryMap = {
    "E-Commerce & Shopping": {
        "General Marketplaces": ["Home", "Search Results", "Product Detail", "Cart", "Checkout", "Payment", "Order Success", "Wishlist", "Reviews"],
        "Grocery & Essentials": ["Store Selection", "Category Grid", "Product List", "Cart Summary", "Time Slot Picker", "Payment", "Order Tracker"],
        "Fashion & Clothing": ["Hero Banner", "Filter Sheet", "Product Gallery", "Size Chart", "Bag", "Checkout", "Returns Dashboard"],
        "Electronics & Gadgets": ["Home", "Product List", "Product Detail", "Comparison Table", "Cart", "Checkout", "Wishlist", "Order Success"],
        "Beauty & Cosmetics": ["Quiz Onboarding", "Recommendation Feed", "AR Try-On Camera", "Review Grid", "Cart", "Subscription Setup"],
        "D2C Brand Apps": ["Brand Hero", "Product Grid", "Customization Studio", "Personalization Preview", "Cart", "Loyalty Dashboard"],
        "Second-hand & Resale": ["Listing Form", "AI Price Tool", "Chat Screen", "Offer Card", "Shipping Label", "Escrow Status"],
        "Furniture & Home Decor": ["AR Measurement Camera", "Room Category", "AR Placement View", "Dimension Check", "Cart", "Delivery Calendar"],
        "Pet Supplies": ["Pet Profile Setup", "Recommended Feed", "Subscription Toggle", "Cart", "Delivery Schedule", "Vaccine Reminder"],
        "Books & Media Stores": ["Search Bar", "Sample Reader", "Review Section", "Wishlist", "Checkout", "Library Downloads"]
    },
    "Healthcare & Telemedicine (Doctors)": {
        "Online Doctor Consultation": ["Symptom Checker", "Doctor Grid", "Time Slot Picker", "Video Call UI", "Prescription PDF", "Follow-up Scheduler"],
        "Medicine Delivery": ["Prescription Scanner", "Interaction Alert", "Cart", "Delivery Calendar", "Payment", "Live Map", "Reminder Settings"],
        "Lab Test Booking": ["Test Grid", "Slot Picker", "Pickup Confirmation", "Status Timeline", "PDF Report", "Chat with Pathologist"],
        "Mental Health Therapy": ["Assessment Quiz", "Match Card", "Booking Calendar", "Therapy Chat", "Exercise Feed", "Mood Graph"],
        "Health Record Storage": ["Biometric Auth", "Scan Camera", "Tagging Interface", "Timeline View", "Share Sheet", "Export Menu"],
        "Dental & Vision Care": ["Service Selection", "Insurance Upload", "Push Notification", "Care Card", "Contact Lens Reorder", "Vision Test History"],
        "Women's Health": ["Calendar Log", "Prediction Card", "Symptom Selector", "Article Feed", "Telemedicine", "PIN Lock"],
        "Physiotherapy & Rehab": ["Assessment Form", "Exercise Video", "Camera Posture Check", "Recovery Graph", "Messaging", "Pain Scale Input"],
        "Pet Healthcare": ["Pet Avatar", "Symptom Selector", "Video Call", "Rx Card", "Order Tracking", "Shot Calendar"],
        "Emergency & First Aid": ["SOS Button", "Location Share", "Dialer", "Video Library", "Map View", "ICE Card"]
    },
    "Personal Assistants & Productivity": {
        "AI Voice Assistants": ["Voice Wave Animation", "Transcript Card", "Result Display", "Action Buttons", "Feedback Thumbs", "Settings"],
        "AI Chatbots (LLMs)": ["Chat Bubble", "Typing Indicator", "Response Stream", "Edit Menu", "Share Sheet", "History List"],
        "Task Management": ["Quick Add", "Calendar Picker", "Priority Badge", "Assignee List", "Notification Settings", "Checkbox", "Recurring Menu"],
        "Calendar & Scheduling": ["Calendar Grid", "Time Slot", "Event Form", "Guest List", "Link Picker", "Sync Status", "Alert Banner"],
        "Email Management": ["Inbox List", "Swipe Icons", "Reader View", "Category Tabs", "Schedule Picker", "Snooze Options"],
        "Password Management": ["Login Screen", "Vault Grid", "Autofill Popup", "Password Generator", "Audit Scorecard", "Secure Share"],
        "Document Scanner": ["Camera View", "Edge Overlay", "Crop Tool", "Filter Slider", "PDF Preview", "OCR Result", "Share Sheet"],
        "Note Taking": ["Blank Canvas", "Format Toolbar", "Drawing Pad", "Media Picker", "Link Button", "Tag Input", "Search Results"],
        "Time Tracking": ["Timer Display", "Start/Pause", "Break Countdown", "Session Log", "Chart View", "CSV Export"],
        "File Transfer": ["File Picker", "QR Code", "Progress Bar", "Speed Meter", "Success Check", "Auto-delete Toggle"]
    },
    "Transportation & Travel (Bus Reservation)": {
        "Bus Booking": ["Location Picker", "Calendar", "Bus List", "Seat Map", "Form Fields", "Payment Gateway", "QR Ticket"],
        "Train Booking": ["Search Bar", "Train Schedule", "Class Toggle", "Passenger Form", "IRCTC Auth", "Payment", "PNR Tracker"],
        "Flight Booking": ["Trip Type Toggle", "Airport Autocomplete", "Calendar", "Passenger Wheel", "Airline Cards", "Extras Menu"],
        "Ride Hailing (Cabs)": ["Map View", "Location Search", "Ride Type Cards", "Confirm Button", "Driver ETA", "Rating Stars", "Tip Selector"],
        "Auto-Rickshaw Booking": ["Map", "Auto Types", "Fare Slider", "Book Button", "OTP Screen", "Cash/UPI", "Receipt"],
        "Car Rental (Self-Drive)": ["Map Picker", "Calendar", "Car Grid", "Document Scanner", "Photo Capture", "Bluetooth Unlock"],
        "Bike & Scooter Rental": ["Map with Icons", "QR Scanner", "Unlock Button", "Ride Timer", "Pause Screen", "Trip Summary"],
        "Public Transit": ["Station Dashboard", "Departure Board", "Route Planner", "Ticket Wallet", "NFC Tap Animation", "Recharge"],
        "Parking & Toll": ["Zone Map", "Start Button", "Countdown Timer", "Payment Methods", "Receipt", "Pass Balance"],
        "EV Charging": ["Map Filters", "Connector Icons", "Slot Booking", "Navigation UI", "Charging Animation", "Payment"]
    },
    "Food & Restaurant": {
        "Food Delivery": ["Map/GPS", "Restaurant Grid", "Menu List", "Item Modal", "Cart Slider", "Payment", "Driver Map", "Rating"],
        "Restaurant Reservation": ["Cuisine Filters", "Time Slots", "Seating Chart", "Pre-order Menu", "Push Reminder", "QR Check-in"],
        "Cloud Kitchen Apps": ["Brand Carousel", "Combo Cards", "Customization Sheet", "Plan Picker", "Calendar", "Live Status"],
        "Grocery Delivery": ["Category Icons", "Product Grid", "Cart Badge", "Timer Widget", "Payment", "Driver Location"],
        "Recipe & Cooking": ["Recipe Feed", "Filter Chips", "Bookmark", "List Export", "Step-by-step", "Video Player", "Rating"],
        "Diet & Nutrition": ["Search Bar", "Barcode Scanner", "Calorie Ring", "Macro Bars", "Goal Slider", "Chart View"],
        "Food Discovery": ["Map Pins", "Filter Sheet", "Photo Grid", "Star Rating", "Camera Upload", "Profile Follow"],
        "Meal Prep": ["Diet Selector", "Weekly Calendar", "Shopping List", "Prep Steps", "Video Tutorials", "Swap Ingredients"],
        "Restaurant POS": ["Menu Grid", "Cart", "Wallet Payment", "QR Code", "Point Balance", "Rewards Catalog", "History Log"]
    },
    "Finance & Banking (FinTech)": {
        "Mobile Banking": ["Face ID", "Balance Card", "Transaction List", "Transfer Form", "Beneficiary List", "Confirmation Slider"],
        "UPI & P2P Payments": ["Amount Pad", "QR Scanner", "Contact List", "PIN Pad", "Success Animation", "Share Sheet"],
        "Expense Tracking": ["Bank Connect", "Category Icons", "Budget Wheel", "Push Notification", "Pie Chart", "AI Prediction"],
        "Bill Payment": ["Biller Grid", "Account Field", "Due Amount", "Payment Methods", "Recurring Toggle", "Calendar Alert"],
        "Stock Trading": ["KYC Form", "Candlestick Chart", "Order Ticket", "Portfolio Pie", "Watchlist Ticker", "News Cards"],
        "Cryptocurrency": ["Wallet Dashboard", "Buy Modal", "Price Graph", "QR Send/Receive", "Stake Pools", "NFT Grid"],
        "Credit Score": ["Score Gauge", "Factor List", "Action Cards", "Dispute Form", "What-if Slider"],
        "Digital Wallets": ["Wallet Card", "NFC Animation", "History Feed", "Split Form", "Card Carousel", "Points Balance"],
        "Savings & Investing": ["Goal Input", "Round-up Toggle", "Auto-debit Slider", "Ring Chart", "Withdraw Button"]
    },
    "Social Media & Communication": {
        "Messaging (Text/IM)": ["Contact Avatar List", "Bubble Chat", "Input Bar", "Camera Roll", "Mic Button", "Voice Note"],
        "Video Calling": ["Contact Card", "Ringing UI", "Grid/Focus View", "Control Buttons", "Share Modal", "End Button"],
        "Social Networks": ["Infinite Scroll Feed", "Action Buttons", "Share Sheet", "Post Composer", "Notification Bell"],
        "Professional Networking": ["Profile Card", "Connect Button", "Job Cards", "Chat Thread", "Skill Badge", "Article Editor"],
        "Dating & Relationships": ["Photo Upload", "Card Stack", "Match Animation", "Chat Screen", "Date Picker", "Video Call"],
        "Live Streaming": ["Preview Screen", "Title Input", "Live Video", "Chat Overlay", "Gift Store", "Mod Tools"],
        "Community Forums": ["Category List", "Thread Title", "Post Detail", "Reply Box", "Vote Arrows", "Flag", "New Thread"],
        "Photo Sharing": ["Camera Roll", "Filter Carousel", "Caption Field", "Tag Input", "Feed", "Search Grid", "Bookmark"],
        "Audio Social": ["Room List", "Stage View", "Hand Icon", "Speaking Indicator", "Listener Count", "Follow Button"]
    },
    "News, Information & Education": {
        "Aggregated News": ["Interest Picker", "Card Swipe", "Article View", "Bookmark", "Share Sheet", "Comment Section"],
        "Online Courses": ["Course Grid", "Enrollment Button", "Video Player", "Quiz Cards", "Upload Assignment", "PDF Certificate"],
        "Language Learning": ["Goal Wheel", "Lesson Card", "Mic Practice", "Multiple Choice", "Streak Fire", "Rank List"],
        "K-12 & Student Tools": ["Class Dashboard", "Assignment List", "Camera Submit", "Test Timer", "Gradebook", "Parent Message"],
        "Competitive Exam": ["Exam Selector", "Live Class Card", "Test Series", "Percentile Predictor", "Chat with Teacher"],
        "Coding & Programming": ["Tutorial Card", "Editor with Highlight", "Run Button", "Error Output", "Challenge List"],
        "Podcasts & Audiobooks": ["Browse Grid", "Subscribe Button", "Episode List", "Player Speed/Timer", "Queue", "Clipper"],
        "Digital Libraries": ["Shelf View", "Borrow Button", "eReader", "Highlighter", "Auto-return", "Hold Queue"],
        "Flashcard & Memorization": ["Deck List", "Card Editor", "Flipping Card", "Quiz Mode", "Mastery Graph", "Export/Import"]
    },
    "Entertainment & Streaming": {
        "Video Streaming (OTT)": ["Plan Selection", "Home Rows", "Player Controls", "Resume Modal", "Thumbs Up/Down", "Continue Row"],
        "Music Streaming": ["Mood Chips", "Playlist Cards", "Now Playing", "Heart Button", "Skip Arrows", "Queue List"],
        "Short-form Video": ["Fullscreen Video", "Like Animation", "Comment Sheet", "Share Menu", "Follow Button", "Sound Picker"],
        "Casual Gaming": ["Splash Screen", "Tutorial Overlay", "Game Canvas", "Coin Counter", "Shop Modal", "Rank List"],
        "Live TV & Sports": ["Program Guide", "Video Player", "Record Button", "Alert Bell", "Clip Reel", "Scorecard"],
        "eSports & Game Streaming": ["Thumbnail Grid", "Live Badge", "Chat Sidebar", "Subscribe Button", "Tip Jar", "Clip Editor"],
        "Karaoke & Music Creation": ["Search", "Scrolling Lyrics", "Record Button", "Pitch Graph", "Effect Rack", "Social Share"],
        "Virtual Events": ["Ticket QR", "Lobby Map", "Avatar Selector", "Stage Video", "Chat Bubble", "Emote Wheel"],
        "Puzzle & Brain Training": ["Daily Card", "Puzzle Grid", "Hint Button", "Countdown", "Rank", "Streak Fire", "Level Map"]
    },
    "Utilities & Tools": {
        "Cloud Storage": ["File Grid", "Upload Button", "Folder Tree", "Share Sheet", "Download Manager", "Green Checkmark"],
        "File Manager": ["Storage Bar", "Directory List", "Checkbox Mode", "Action Bar", "Search Results", "Zip Preview"],
        "Weather": ["Weather Card", "Hourly Scroll", "Weekly List", "Animated Radar", "Red Alert Banner"],
        "Navigation & Maps": ["Search Bar", "Route Cards", "Turn-by-turn", "Voice Bubble", "ETA Bar", "Destination Image"],
        "Device Cleaner": ["Scan Button", "File Size List", "Clean Button", "Boost Animation", "Battery Graph", "Temp Gauge"],
        "VPN & Privacy": ["Connect Toggle", "Server List", "Map Animation", "Speed Graph", "Kill Switch Toggle", "App List"],
        "QR & Barcode Scanner": ["Camera Overlay", "Alignment Guide", "Result Popup", "Action Buttons", "Scan History"],
        "Calculator": ["Button Grid", "Formula Entry", "History Drawer", "Constant Picker", "Graph View", "Unit Tabs"],
        "Unit Converter": ["Category Picker", "Input Field", "Rate Display", "Swap Button", "Star Icon", "Offline Badge"],
        "Screen Recorder": ["Settings Menu", "Record Button", "3-2-1 Countdown", "Stop Notification", "Trim Tool", "Share"]
    },
    "Home & Lifestyle Management": {
        "Grocery List": ["Add Bar", "Category Tabs", "Checkbox List", "Sort Menu", "Share Sheet", "Cloud Sync"],
        "Home Services": ["Issue Form", "Camera Upload", "Quote Card", "Calendar", "Live Location", "Payment", "Star Rating"],
        "Real Estate & Rental": ["Filter Sheet", "Map Pins", "Photo Gallery", "Agent Chat", "Calendar", "Application Form"],
        "Interior Design (AR)": ["AR Measure", "Floor Plan", "3D Model", "Drag Handle", "Save Button", "Buy Link", "Social Share"],
        "Smart Home Control": ["Device Grid", "Toggle Switch", "Scene Buttons", "Mic Icon", "Timer", "Geofence", "Usage Chart"],
        "Gardening & Plant Care": ["Camera", "ID Result", "Health Card", "Water Calendar", "Reminder Bell", "Store Link"],
        "Home Security": ["Dashboard Shield", "Camera Feed", "Notification List", "Playback", "Mic Button", "Panic Button"],
        "Cleaning & Chores": ["Task List", "Point Badge", "Due Date", "Checkbox", "Reward Store", "Rank", "Reset Button"],
        "Solar & Energy": ["Power Flow Diagram", "Consumption Graph", "Export Meter", "Savings Card", "Weather Widget"]
    },
    "Fitness, Health & Wellness": {
        "Step Tracking": ["Step Ring", "Goal Progress", "Map Route", "Calorie Burn", "Weekly Bar", "Badge Case", "Challenge Card"],
        "Workout & Gym": ["Muscle Map", "Plan Card", "Video Player", "Counter Buttons", "Timer", "Log Sheet", "Strength Graph"],
        "Yoga & Pilates": ["Level Selector", "Session Card", "Video", "Skeleton Overlay", "Hold Clock", "Modify Button"],
        "Running & Cycling": ["Start Button", "Pace Display", "HR Graph", "Voice Notification", "Map Trail", "Splits Table"],
        "Sleep Tracking": ["Night Mode", "Sleep Graph", "Stage Colors", "Snore Timeline", "Score Ring", "Advice Card"],
        "Meditation": ["Duration Slider", "Sound Picker", "Voice Guide", "Breathing Circle", "Mood Emoji", "Streak Flame"],
        "Weight Lifting": ["Workout Builder", "Exercise Search", "Input Fields", "Rest Clock", "1RM Display", "Volume Graph"],
        "Heart Rate Monitor": ["Camera Lens", "Timer", "BPM Display", "HRV Card", "Zone Graph", "Trend Line"],
        "Workout Plan Builders": ["Goal Selector", "Days Slider", "Equipment Toggle", "Generated Plan", "Edit Mode"]
    },
    "Travel & Accommodation": {
        "Hotel Booking": ["Location", "Calendar", "Guest Picker", "Search Button", "Filter Sheet", "Room Cards", "Payment", "PDF Voucher"],
        "Homestays & Rentals": ["Map Pins", "Photo Gallery", "Amenity Icons", "Chat Bubble", "Calendar", "Door Code", "Star Rating"],
        "Hostel Booking": ["Bed Map", "Gender Toggle", "Event List", "Check-in QR", "Common Room Chat"],
        "Last Minute Deals": ["Map", "Timer Countdown", "Price Slash", "Book Button", "Wallet Key"],
        "Travel Insurance": ["Itinerary Form", "Coverage Toggles", "Price Quote", "Payment", "PDF Viewer", "Claim Upload", "SOS"],
        "Tour & Activity": ["Category Grid", "Calendar", "Time Picker", "QR Code", "Scanner", "Star Rating", "Tip Amount"],
        "Visa & Documents": ["Document Scanner", "Country Dropdown", "Form Wizard", "Camera", "Payment", "Shipping Label"],
        "Luggage Storage": ["Map Icons", "Hour Selector", "QR Tag", "GPS Tracking", "Release Code", "Wallet", "Rating"],
        "Group Travel": ["Trip Card", "Contact Picker", "Poll UI", "Collaborative Calendar", "Splitwise Integration", "Group Chat"]
    },
    "Dating & Relationships": {
        "Swipe-based Dating": ["Profile Builder", "Card Stack", "Like/Pass Buttons", "Match Animation", "Chat Screen", "Date Picker"],
        "Serious Relationships": ["Quiz Pages", "Score Ring", "Match List", "Icebreaker Qs", "Video Call", "Date Venue"],
        "LGBTQ+ Focused": ["Tribe Picker", "Pronoun Badges", "Profile Grid", "Chat", "Event Map", "Forum"],
        "Niche & Interests": ["Tag Cloud", "Filter", "Cooldown Timer", "Hobby Highlight", "Event Card", "Group Invite"],
        "Video-first Dating": ["Video Feed", "Heart Button", "Match Popup", "Call UI", "Mini Games", "Calendar"],
        "Matrimony": ["Parent Dashboard", "Kundli Score", "Verified Badge", "Gallery", "Secure Chat", "Meeting Request"],
        "Relationship Health": ["Partner Link", "Question Card", "Send Love", "Idea Generator", "Therapy Tips", "Calendar Alert"],
        "Faith-based Dating": ["Faith Selector", "Prayer Widget", "Dietary Toggle", "Place Map", "Family Chat", "Ceremony Planner"]
    },
    "Career, Job Search & Freelancing": {
        "Job Portals": ["Resume Parser", "Search Filters", "Apply Button", "Status Timeline", "Calendar", "Offer Letter", "Docs Upload"],
        "Freelancing Platforms": ["Gig Form", "Portfolio Grid", "Bid Modal", "Chat", "Milestone Slider", "Escrow", "Star Rating"],
        "Remote Job Boards": ["Remote Toggle", "Timezone Slider", "Video Interview", "Test Module", "E-sign", "Equipment List"],
        "Resume Builder": ["Template Gallery", "Form Fields", "AI Tips", "Score Meter", "PDF Export", "Shareable Link"],
        "Interview Prep": ["Role Selector", "Camera", "Question Display", "Record Button", "Feedback Card", "Practice Again"],
        "Gig Economy": ["Map", "Online Toggle", "Job Card", "GPS Route", "Finish Button", "Wallet", "Rating"],
        "Side Hustle": ["Task Cards", "Instructions", "Camera Upload", "Status", "Withdraw Button", "Streak"],
        "Career Coaching": ["Coach Profiles", "Calendar", "Goal Form", "Call UI", "PDF Plan", "Check-in"]
    },
    "Photography & Video Editing": {
        "Photo Editing (Basic)": ["Gallery Picker", "Crop Grid", "Sliders", "Filter Row", "Export Button", "Share Sheet"],
        "Photo Editing (Advanced)": ["Layer Panel", "Mask Overlay", "Curve Graph", "Brush Tool", "Wheels", "Save as PSD"],
        "Video Editing (Basic)": ["Timeline", "Trim Handles", "Transition Icons", "Text Overlay",
