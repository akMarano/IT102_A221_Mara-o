import streamlit as st

from user import User
from ride_processing import RideProcessor, RideOffer, RideRequest

DAYS = ["S", "M", "T", "W", "T", "F", "S"]

if "processor" not in st.session_state:
    st.session_state.processor = RideProcessor()
if "page" not in st.session_state:
    st.session_state.page = "dashboard"
if "selected_offer" not in st.session_state:
    st.session_state.selected_offer = None
if "selected_request" not in st.session_state:
    st.session_state.selected_request = None

processor = st.session_state.processor


def go_to(page, offer=None, request=None):
    st.session_state.page = page
    if offer is not None:
        st.session_state.selected_offer = offer
    if request is not None:
        st.session_state.selected_request = request


def show_dashboard():
    st.title("Ride Dashboard")

    col1, col2 = st.columns(2)
    col1.button("Post Ride Offer", use_container_width=True,
                on_click=go_to, args=("post_offer",))
    col2.button("Post Ride Request", use_container_width=True,
                on_click=go_to, args=("post_request",))

    st.text_input("Search origin")
    st.text_input("Search destination")

    tab1, tab2 = st.tabs(["Ride Offers", "Ride Requests"])

    with tab1:
        for offer in processor.get_offers():
            with st.container(border=True):
                c1, c2 = st.columns([3, 1])
                c1.write(f"**{offer.driver.name}** ⭐ {offer.driver.rating} "
                         f"({offer.driver.trips} rides)")
                c1.write(f"{offer.origin} → {offer.destination}")
                c2.button("View", key=f"view_offer_{id(offer)}",
                          on_click=go_to, args=("ride_details", offer))

    with tab2:
        for request in processor.get_requests():
            with st.container(border=True):
                c1, c2 = st.columns([3, 1])
                c1.write(f"**{request.rider.name}** ⭐ {request.rider.rating} "
                         f"({request.rider.trips} rides)")
                c1.write(f"{request.origin} → {request.destination}")
                c2.button("View", key=f"view_request_{id(request)}",
                          on_click=go_to, args=("request_details", None, request))


def show_post_offer():
    st.button("← Back", on_click=go_to, args=("dashboard",))
    st.title("Post Ride Offer")

    st.subheader("Route Details")
    origin = st.text_input("Origin")
    destination = st.text_input("Destination")
    contribution = st.number_input("Contribution (₱)", min_value=0, step=1)
    seats = st.number_input("Seats Available", min_value=1, step=1)

    st.subheader("Schedule")
    date = st.date_input("Date")
    time = st.time_input("Time")
    recurring = st.toggle("Recurring Ride")
    days = []
    if recurring:
        st.write("Repeat on:")
        day_cols = st.columns(len(DAYS))
        for i, (col, day) in enumerate(zip(day_cols, DAYS)):
            if col.checkbox(day, key=f"offer_day_{i}"):
                days.append(day)

    notes = st.text_area("Driver's Notes")

    if st.button("Submit Offer"):
        driver = User("You", 5.0, 0)
        offer = RideOffer(driver, origin, destination, contribution, seats,
                           date, time, recurring, days, notes)
        processor.submit_offer(offer)
        go_to("dashboard")


def show_post_request():
    st.button("← Back", on_click=go_to, args=("dashboard",))
    st.title("Post Ride Request")

    st.subheader("Route Details")
    origin = st.text_input("Origin")
    destination = st.text_input("Destination")
    contribution = st.number_input("Contribution (₱)", min_value=0, step=1)

    st.subheader("Schedule")
    date = st.date_input("Date")
    time = st.time_input("Time")
    recurring = st.toggle("Recurring Request")
    days = []
    if recurring:
        st.write("Repeat on:")
        day_cols = st.columns(len(DAYS))
        for i, (col, day) in enumerate(zip(day_cols, DAYS)):
            if col.checkbox(day, key=f"request_day_{i}"):
                days.append(day)

    notes = st.text_area("Rider's Notes")

    if st.button("Submit Request"):
        rider = User("You", 5.0, 0)
        request = RideRequest(rider, origin, destination, contribution,
                               date, time, recurring, days, notes)
        processor.submit_request(request)
        go_to("dashboard")


def show_ride_details():
    st.button("← Back", on_click=go_to, args=("dashboard",))
    offer = st.session_state.selected_offer
    st.title("Ride Details")

    st.write(f"**{offer.driver.name}** ⭐ {offer.driver.rating} "
             f"({offer.driver.trips} rides)")
    st.text_input("Origin", value=offer.origin)
    st.text_input("Destination", value=offer.destination)
    st.date_input("Date", value=offer.date)
    st.time_input("Time", value=offer.time)
    st.text_area("Driver's Notes", value=offer.notes)


def show_request_details():
    st.button("← Back", on_click=go_to, args=("dashboard",))
    request = st.session_state.selected_request
    st.title("Ride Request Details")

    st.write(f"**{request.rider.name}** ⭐ {request.rider.rating} "
             f"({request.rider.trips} rides)")
    st.text_input("Origin", value=request.origin)
    st.text_input("Destination", value=request.destination)
    st.date_input("Date", value=request.date)
    st.time_input("Time", value=request.time)
    st.text_area("Rider's Notes", value=request.notes)


pages = {
    "dashboard": show_dashboard,
    "post_offer": show_post_offer,
    "post_request": show_post_request,
    "ride_details": show_ride_details,
    "request_details": show_request_details,
}

pages[st.session_state.page]()