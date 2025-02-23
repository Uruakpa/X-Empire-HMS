from django.urls import path
from .views import *



urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name="home"),
    path('events/', events, name="events"),
    path('announcements/', announcements, name="announcements"),
    path('event-profile/<str:id>/', event_profile, name="event-profile"),
    path('event-edit/<str:pk>/', event_edit, name="event-edit"),
    path('error/', error, name="error"),
    path('payment/', payment, name="payment"),
    path('verify/', verify, name="verify"),
    path('deleteStorage/<str:pk>/', deleteStorage, name="deleteStorage"),
    path('deleteFoodMenu/<str:pk>/', deleteFoodMenu, name="deleteFoodMenu"),
    path('food-menu/', food_menu, name="food-menu"),
    path('storage/', storage, name="storage"),
    path('food-menu/<str:pk>/', food_menu_edit, name="food-menu-edit"),
    path('createEvent/', createEvent, name="createEvent"),
    path('deleteEvent/<str:pk>/', deleteEvent, name="deleteEvent"),
    path('deleteAnnouncement/<str:pk>/',
         deleteAnnouncement, name="deleteAnnouncement"),
    path('accounts/<str:pk>/', accounts_page, name='accounts'),
    path('dashboard/<str:pk>/', index_page, name='dashboard'),
    path('transactions/<str:pk>/', transaction_page, name="transaction"),
    path('room_booking_list/<str:pk>/', room_booking_list, name="room-booking-list"),
    path('room_booking/<str:pk>/', room_booking, name="room-booking"),
    path('check_in_out/<str:pk>/', reservations, name="checkin-out"),
    path('room-status/<str:pk>/', room_status, name="room-status"),
    path('item-unit-list/<str:pk>/', item_unit_list, name="item-unit-list"),
    path('item-list/<str:pk>/', item_list, name="item-list"),
    path('item-destroyed-list/<str:pk>/', item_destroyed_list, name="item-destroyed-list"),
    path('item-category-list/<str:pk>/', item_category_list, name="item-category-list"),
    path('item-suppliers-list/<str:pk>/', item_suppliers_list, name="item-suppliers-list"),
    path('booking-report/<str:pk>/', booking_report, name="booking-report"),
    path('stock-report/<str:pk>/', stuck_report, name="stock-report"),
    path('purchase-report/<str:pk>/', purchase_report, name="purchase-report"),
    path('Financial/<str:pk>/', financial, name="Financial"),
    path('Financial_ending/<str:pk>/', financial_ending, name="Financial_ending"),
    path('chart_of_account/<str:pk>/', chart_of_account, name="chart_of_account"),
    path('opening_balance/<str:pk>/', opening_balance, name="opening_balance"),
    path('debit_voucher/<str:pk>/', debit_voucher, name="debit_voucher"),
    path('credit_voucher/<str:pk>/', credit_voucher, name="credit_voucher"),
    path('contra_voucher/<str:pk>/', contra_voucher, name="contra_voucher"),
    path('journal_voucher/<str:pk>/', journal_voucher, name="journal_voucher"),
    path('voucher_approval/<str:pk>/', voucher_approval, name="voucher_approval"),
    path('voucher_report/<str:pk>/', voucher_report, name="voucher_report"),
    path('cash_book/<str:pk>/', cash_book, name="cash_book"),
    path('general_ledger/<str:pk>/', general_ledger, name="general_ledger"),
    path('trial_balance/<str:pk>/', trial_balance, name="trial_balance"),
    path('profit_loss/<str:pk>/', profit_loss, name="profit_loss"),
    path('coa_print/<str:pk>/', coa_print, name="coa_print"),
    path('store/<str:pk>/',store, name="store"),
    path('housekeeping_roomcleaning/<str:pk>/', housekeeping_roomcleaning, name="housekeeping_roomcleaning"),
    # path('restaurant/<str:pk>/', restaurant, name="restaurant"),
    path('balance_sheet/<str:pk>/', balance_sheet, name="balance_sheet"),
    path('checkin/<int:pk>/', checkin_out, name="checkin"),
    path('checkout/<int:pk>/', checkin_payment, name="checkout"),
    # path('bar/<int:pk>/', bar, name="bar"),
    
    # path('hotel/<int:pk>/', checkin_out, name="h"),
    # path('transaction', transaction, name="purchase-report"),
    # path('frontdesk/<str:pk>/', front_desk, name="front-desk"),
    # path('admin-page/<str:pk>/', admin_page, name="admin-page"),
    
]
