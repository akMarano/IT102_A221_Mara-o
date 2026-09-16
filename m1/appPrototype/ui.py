import datetime

import streamlit as st

from user import User
from ride_processing import RideProcessor, RideOffer, RideRequest

DAYS = ["S", "M", "T", "W", "T", "F", "S"]

st.set_page_config(page_title="SabaySakay", layout="wide")

if "processor" not in st.session_state:
    st.session_state.processor = RideProcessor()
    # Sample Data
    sample_drivers = [
        User("Maria Santos", 4.9, 128),
        User("Carlo Reyes", 4.7, 64),
        User("Anna Lim", 5.0, 212),
        User("Paolo Cruz", 4.6, 37),
    ]
    sample_routes = [
        ("Matina", "Ateneo de Davao"),
        ("Bajada", "Lanang"),
        ("Toril", "Downtown Davao"),
        ("Buhangin", "SM Ecoland"),
    ]
    for driver, (origin, dest) in zip(sample_drivers, sample_routes):
        st.session_state.processor.submit_offer(
            RideOffer(
                driver, origin, dest, 50, 3,
                datetime.date.today(), datetime.time(8, 0),
            )
        )

    sample_riders = [
        User("Nico Villanueva", 4.8, 42),
        User("Bea Fernandez", 4.6, 19),
        User("Miguel Santos", 5.0, 87),
        User("Ella Ramos", 4.9, 53),
    ]
    sample_request_routes = [
        ("Ma-a", "USeP"),
        ("Catalunan Grande", "Abreeza Mall"),
        ("Talomo", "Davao Doctors Hospital"),
        ("Panacan", "Davao Airport"),
    ]
    for rider, (origin, dest) in zip(sample_riders, sample_request_routes):
        st.session_state.processor.submit_request(
            RideRequest(
                rider, origin, dest, 45,
                datetime.date.today(), datetime.time(9, 30),
            )
        )

if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True
if "page" not in st.session_state:
    st.session_state.page = "dashboard"
if "selected_offer" not in st.session_state:
    st.session_state.selected_offer = None
if "selected_request" not in st.session_state:
    st.session_state.selected_request = None
if "offer_seats" not in st.session_state:
    st.session_state.offer_seats = 1

processor = st.session_state.processor


def go_to(page, offer=None, request=None):
    st.session_state.page = page
    if offer is not None:
        st.session_state.selected_offer = offer
    if request is not None:
        st.session_state.selected_request = request


def toggle_sidebar():
    st.session_state.sidebar_open = not st.session_state.sidebar_open


st.markdown(
    """
    <style>
    .ride-card {
        background-color: #1e1e1e;
        color: #ffffff;
        border-radius: 8px;
        padding: 14px 18px;
        margin-bottom: 10px;
        min-height: 90px;
    }
    .ride-card .route {
        font-size: 0.9rem;
        color: #cccccc;
    }
    .avatar-circle {
        width: 56px;
        height: 56px;
        border-radius: 50%;
        background-color: #e0e0e0;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.4rem;
        font-weight: 600;
        color: #555555;
        margin-bottom: 8px;
    }
    .map-placeholder {
        width: 100%;
        height: 220px;
        border-radius: 8px;
        background: repeating-linear-gradient(45deg, #d9d9d9, #d9d9d9 10px, #e9e9e9 10px, #e9e9e9 20px);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #888888;
        font-size: 0.9rem;
        border: 1px solid #cccccc;
        margin-bottom: 12px;
    }
    .st-key-offer_seats_count button {
        border: none !important;
        background: transparent !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        cursor: default !important;
        opacity: 1 !important;
        pointer-events: none;
    }
    .st-key-seat_stepper div[data-testid="stHorizontalBlock"] {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 14px;
    }
    .st-key-seat_stepper div[data-testid="column"] {
        width: auto !important;
        flex: none !important;
        min-width: 0 !important;
    }
    .st-key-seat_stepper div[data-testid="stVerticalBlock"] {
        gap: 0 !important;
    }
    .st-key-seat_stepper div[data-testid="element-container"] {
        margin: 0 !important;
    }
    .st-key-seat_stepper button {
        width: 40px !important;
        height: 38px !important;
    }

    /* ---------- sidebar ---------- */
    section[data-testid="stSidebar"] {
        border-right: 2px solid #000000;
    }
    .profile-block {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        padding: 6px 0 18px 0;
        border-bottom: 2px solid #000000;
        margin-bottom: 12px;
    }
    .profile-avatar {
        width: 56px;
        height: 56px;
        border-radius: 50%;
        border: 2px solid #000000;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.6rem;
        margin-bottom: 8px;
    }
    .profile-name {
        font-weight: 700;
        font-size: 1.05rem;
    }
    .profile-sub {
        font-size: 0.8rem;
        color: #888888;
    }
    .st-key-sidebar_nav button {
        text-align: left !important;
        justify-content: flex-start !important;
        background: transparent !important;
        border: none !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
        padding-left: 4px !important;
    }
    .st-key-sidebar_nav button:hover {
        color: #555555 !important;
    }
    .st-key-logout_block button {
        border: 2px solid #000000 !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
    }

    /* ---------- dashboard search bar ---------- */
    .st-key-search_block div[data-testid="stTextInput"] input {
        height: 90px;
        border-radius: 8px;
    }

    /* icon-only filter button */
    .st-key-filter_block button {
        border-radius: 8px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if not st.session_state.sidebar_open:
    st.markdown(
        """
        <style>
        section[data-testid="stSidebar"] {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def back_button():
    col1, col2 = st.columns([1, 30])
    with col1:
        st.button("←", key=f"back_{st.session_state.page}", on_click=go_to, args=("dashboard",))
    with col2:
        st.button("☰", key=f"menu_{st.session_state.page}", on_click=toggle_sidebar)


def show_sidebar():
    with st.sidebar:
        st.markdown(
            """
            <div class="profile-block">
                <div class="profile-avatar">👤</div>
                <div class="profile-name">Arem Kein I. Marano</div>
                <div class="profile-sub">Profile Details</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.container(key="sidebar_nav"):
            st.button(
                "⊞  Dashboard",
                key="nav_dashboard",
                use_container_width=True,
                on_click=go_to,
                args=("dashboard",),
            )
            st.button("🚗  Ride History", key="nav_history", use_container_width=True)
            st.button("💬  Ride Chats", key="nav_chats", use_container_width=True)

        st.markdown("<div style='height: 260px;'></div>", unsafe_allow_html=True)

        with st.container(key="logout_block"):
            st.button("Logout", key="logout_button", use_container_width=True)


def show_dashboard():
    st.button("☰", key="menu_button", on_click=toggle_sidebar)

    actions_col, search_col = st.columns([3, 2])

    with actions_col:
        row1_col1, row1_col2 = st.columns(2)
        with row1_col1:
            st.button(
                "Post ride offer",
                use_container_width=True,
                on_click=go_to,
                args=("post_offer",),
            )
        with row1_col2:
            st.button(
                "Post ride request",
                use_container_width=True,
                on_click=go_to,
                args=("post_request",),
            )

        row2_col1, row2_col2 = st.columns(2)
        with row2_col1:
            st.button("Ride History", key="dash_history", use_container_width=True)
        with row2_col2:
            st.button("Ride Chats", key="dash_chats", use_container_width=True)

    with search_col:
        with st.container(key="search_block"):
            search_text = st.text_input(
                "Search", placeholder="Search rides", label_visibility="collapsed"
            )

    filler_col, filter_col = st.columns([10, 1])
    with filter_col:
        with st.container(key="filter_block"):
            st.button("🎚️", key="filters_button", help="Filters")

    search_text = (search_text or "").lower()

    tab1, tab2 = st.tabs(["Ride Offers", "Ride Requests"])

    with tab1:
        offers = [
            o
            for o in processor.get_offers()
            if search_text in o.origin.lower() or search_text in o.destination.lower()
        ]
        if not offers:
            st.caption("No ride offers yet.")
        cols = st.columns(2)
        for i, offer in enumerate(offers):
            with cols[i % 2]:
                st.markdown(
                    f"""
                    <div class="ride-card">
                        <b>{offer.driver.name}</b> ⭐ {offer.driver.rating}
                        ({offer.driver.trips} rides)<br/>
                        <span class="route">{offer.origin} → {offer.destination}</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.button(
                    "View",
                    key=f"view_offer_{id(offer)}",
                    on_click=go_to,
                    args=("ride_details", offer),
                    use_container_width=True,
                )

    with tab2:
        requests = [
            r
            for r in processor.get_requests()
            if search_text in r.origin.lower() or search_text in r.destination.lower()
        ]
        if not requests:
            st.caption("No ride requests yet.")
        cols = st.columns(2)
        for i, request in enumerate(requests):
            with cols[i % 2]:
                st.markdown(
                    f"""
                    <div class="ride-card">
                        <b>{request.rider.name}</b> ⭐ {request.rider.rating}
                        ({request.rider.trips} rides)<br/>
                        <span class="route">{request.origin} → {request.destination}</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.button(
                    "View",
                    key=f"view_request_{id(request)}",
                    on_click=go_to,
                    args=("request_details", None, request),
                    use_container_width=True,
                )

def show_post_offer():
    back_button()
    st.title("Post Ride Offer")

    route_col, schedule_col = st.columns(2)

    with route_col:
        st.subheader("Route Details")
        origin = st.text_input("Origin", key="offer_origin")
        destination = st.text_input("Destination", key="offer_destination")

        contribution_col, seats_col = st.columns(2)
        with contribution_col:
            contribution = st.number_input(
                "Contribution (₱)", min_value=0, step=1, key="offer_contribution"
            )
        with seats_col:
            st.write("Seats Available")
            with st.container(key="seat_stepper"):
                minus_col, count_col, plus_col = st.columns(
                    [1, 1, 1], vertical_alignment="center"
                )
                if minus_col.button("−", key="offer_seats_minus"):
                    st.session_state.offer_seats = max(1, st.session_state.offer_seats - 1)
                count_col.button(
                    str(st.session_state.offer_seats),
                    key="offer_seats_count",
                    disabled=True,
                    use_container_width=True,
                )
                if plus_col.button("+", key="offer_seats_plus"):
                    st.session_state.offer_seats += 1

    with schedule_col:
        st.subheader("Schedule")
        date_col, time_col = st.columns(2)
        with date_col:
            date = st.date_input("Date", key="offer_date")
        with time_col:
            time = st.time_input("Time", key="offer_time")

        recurring = st.toggle("Recurring Ride", key="offer_recurring")
        days = []
        if recurring:
            st.write("Repeat on:")
            day_cols = st.columns(len(DAYS))
            for i, (col, day) in enumerate(zip(day_cols, DAYS)):
                if col.checkbox(day, key=f"offer_day_{i}"):
                    days.append(day)

        st.write("Driver's Notes")
        notes = st.text_area("Driver's Notes", key="offer_notes", label_visibility="collapsed")

    if st.button("Submit Offer", use_container_width=True):
        driver = User("You", 5.0, 0)
        offer = RideOffer(
            driver,
            origin,
            destination,
            contribution,
            st.session_state.offer_seats,
            date,
            time,
            recurring,
            days,
            notes,
        )
        processor.submit_offer(offer)
        st.session_state.offer_seats = 1
        go_to("dashboard")

def show_post_request():
    back_button()
    st.title("Post Ride Request")

    route_col, schedule_col = st.columns(2)

    with route_col:
        st.subheader("Route Details")
        origin = st.text_input("Origin", key="request_origin")
        destination = st.text_input("Destination", key="request_destination")
        contribution = st.number_input(
            "Contribution (₱)", min_value=0, step=1, key="request_contribution"
        )

    with schedule_col:
        st.subheader("Schedule")
        date_col, time_col = st.columns(2)
        with date_col:
            date = st.date_input("Date", key="request_date")
        with time_col:
            time = st.time_input("Time", key="request_time")

        recurring = st.toggle("Recurring Request", key="request_recurring")
        days = []
        if recurring:
            st.write("Repeat on:")
            day_cols = st.columns(len(DAYS))
            for i, (col, day) in enumerate(zip(day_cols, DAYS)):
                if col.checkbox(day, key=f"request_day_{i}"):
                    days.append(day)

        st.write("Rider's Notes")
        notes = st.text_area("Rider's Notes", key="request_notes", label_visibility="collapsed")

    if st.button("Submit Request", use_container_width=True):
        rider = User("You", 5.0, 0)
        request = RideRequest(
            rider, origin, destination, contribution, date, time, recurring, days, notes
        )
        processor.submit_request(request)
        go_to("dashboard")

def show_ride_details():
    back_button()
    offer = st.session_state.selected_offer
    st.title("Ride Details")

    info_col, map_col = st.columns(2)

    with info_col:
        initial = offer.driver.name[0].upper() if offer.driver.name else "?"
        st.markdown(f"<div class='avatar-circle'>{initial}</div>", unsafe_allow_html=True)
        st.markdown(f"**{offer.driver.name}**  ⭐ {offer.driver.rating} ({offer.driver.trips} rides)")

        st.text_input("Origin", value=offer.origin, disabled=True)
        st.text_input("Destination", value=offer.destination, disabled=True)

        contribution_col, seats_col = st.columns(2)
        contribution_col.text_input("Contribution", value=f"₱{offer.contribution}", disabled=True)
        seats_col.text_input("Seats Available", value=str(offer.seats), disabled=True)

        st.button("Request to Join", use_container_width=True)

    with map_col:
        st.markdown(
            "<div class='map-placeholder'>Map preview not available</div>",
            unsafe_allow_html=True,
        )
        date_col, time_col = st.columns(2)
        date_col.text_input("Date", value=str(offer.date), disabled=True)
        time_col.text_input("Time", value=str(offer.time), disabled=True)
        st.text_area("Driver's Notes", value=offer.notes, disabled=True)


def show_request_details():
    back_button()
    request = st.session_state.selected_request
    st.title("Ride Request Details")

    info_col, map_col = st.columns(2)

    with info_col:
        initial = request.rider.name[0].upper() if request.rider.name else "?"
        st.markdown(f"<div class='avatar-circle'>{initial}</div>", unsafe_allow_html=True)
        st.markdown(
            f"**{request.rider.name}**  ⭐ {request.rider.rating} ({request.rider.trips} rides)"
        )

        st.text_input("Origin", value=request.origin, disabled=True)
        st.text_input("Destination", value=request.destination, disabled=True)
        st.text_input("Contribution", value=f"₱{request.contribution}", disabled=True)

        st.button("Offer a Ride", use_container_width=True)

    with map_col:
        st.markdown(
            "<div class='map-placeholder'>Map preview not available</div>",
            unsafe_allow_html=True,
        )
        date_col, time_col = st.columns(2)
        date_col.text_input("Date", value=str(request.date), disabled=True)
        time_col.text_input("Time", value=str(request.time), disabled=True)
        st.text_area("Rider's Notes", value=request.notes, disabled=True)


pages = {
    "dashboard": show_dashboard,
    "post_offer": show_post_offer,
    "post_request": show_post_request,
    "ride_details": show_ride_details,
    "request_details": show_request_details,
}

show_sidebar()
pages[st.session_state.page]()