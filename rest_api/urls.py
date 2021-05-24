from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.views.decorators.csrf import csrf_exempt
from rest_framework.urlpatterns import format_suffix_patterns
from rest_api import views as api_view

urlpatterns = (
    url(r'^restapi_test/$', api_view.restapi_test, name="restapi_test"),
#     url(r'^ques_choice/(?P<cat_slug>[\w-]+)/$', api_view.SurveyQuestionChoices.as_view() , name='ques_choices'),
#     url(r'^raisec_outcome/$', api_view.UserRiasecSurveyDetails.as_view() , name='rsc_usrdtls'),
# #     url(r'^ques_choice/(?P<cat_slug>[\w-]+)/$', api_view.assessment_ques_choices_list , name='ques_choices'),
#     url(r'^report_riasec/$', api_view.ReportPersonalitySurvey.as_view() , name='report_riasec'),
#     url(r'^report_cluster/$', api_view.ReportClusterSurvey.as_view() , name='report_cluster'),
#     url(r'^myprofile/$', api_view.user_profile, name='myprofile'),
#     url(r'^trans_lite_login/$', csrf_exempt(api_view.trans_lite_login), name='trans_lite_login'),
#     url(r'^trans_lite_logout/$', api_view.trans_lite_logout, name='trans_lite_logout'),
#     url(r'^change_password/$', api_view.change_password, name='change_password'),
#     url(r'^mydashboard/$', api_view.MyDashboard.as_view(), name="mydashboard"),
#     url(r'^get_country_state_city/$', api_view.get_country_state_city, name="get_country_state_city"),
# #     url(r'^get_state_city/(?P<category>[\w-]+)/(?P<type>[\w-]+)$', api_view.get_country_state_city, name="get_state_city"),
#     url(r'^profile_details/(?P<slug>[\w-]+)$', api_view.profile_details, name="profile_details"),
#     url(r'^profile_details/(?P<slug>[\w-]+)/(?P<crud>[\w-]+)$', api_view.profile_details, name="profile_details"),
#     url(r'^profile_details/(?P<slug>[\w-]+)/(?P<crud>[\w-]+)/(?P<type_id>[\w-]+)$', api_view.profile_details, name="profile_details"),
#     url(r'^networking/$', api_view.networking_details, name="networking"),
#     url(r'^networking_search/(?P<type>[\w-]+)$', api_view.networking_search_details, name="networking_search"),
#     url(r'^same_minded_peers/(?P<type>[\w-]+)$', api_view.same_minded_peers_in_city, name='same_minded_peers'),
#     #url(r'^connected_users/$', api_view.get_network_connected_users, name='connected_users'),
#     #url(r'^requests_received/$', api_view.network_requests_received, name='requests_received'),
#     #url(r'^requests_sent/$', api_view.network_requests_sent, name='requests_sent'),
#     url(r'^friend_request_dtls/(?P<type>[\w-]+)/(?P<selcted_user>[\w-]+)$', api_view.friend_request_details, name="friend_request_details"),
#     url(r'^wow_selected_option/(?P<type>[\w-]+)/$', api_view.wow_selected_option, name="wow_selected_option"),
#     url(r'^wol_selected_option/(?P<type>[\w-]+)/$', api_view.wol_selected_option, name="wol_selected_option"),
#     url(r'^wow_comparision/$', api_view.wow_comparision, name="wow_comparision"),
#     url(r'^wol_comparision/$', api_view.wol_comparision, name="wol_comparision"),
#     url(r'^choose_wol_option/(?P<action>[\w-]+)/(?P<type_id>[\w-]+)$', api_view.choose_wol_option, name="choose_wol_option"),
#     url(r'^notification/$', api_view.notification_details, name="notification"),
#     url(r'^notification_edit/(?P<type>[\w-]+)/(?P<notify_id>[\w-]+)$', api_view.notification_edit, name="notification_edit"),
#     url(r'^wow_option_summary/(?P<occ_id>[\w-]+)$', api_view.get_wow_selected_summary, name="wow_selected_summary"),
#     url(r'^explore_wow_dtl/$', api_view.explore_wow_search_details, name="explore_wow_dtl"),
#     url(r'^wow_autocomplete/(?P<type>[\w-]+)$', api_view.wow_category_autocomplete, name="wow_autocomplete"),
#     url(r'^explore_wol_dtl/$', api_view.explore_wol_search_details, name="explore_wol_dtl"),
#     url(r'^get_riasec_options/$', api_view.get_riasec_options, name="get_riasec_options"),
#     url(r'^wol_autocomplete/(?P<type>[\w-]+)$', api_view.fos_stream_catcomplete, name="wol_autocomplete"),
#     url(r'^representative_dashboard/$', api_view.representative_dashboard, name="representative_dashboard"),
#     url(r'^student_details/(?P<type>[\w-]+)$', api_view.bulkupload_student_details, name="student_details"),
#     url(r'^live_notify_count/$', api_view.get_unread_notification_count, name="live_notify_count"),
#     url(r'^get_riasec_occupation/$', api_view.get_riasec_occupation, name="get_riasec_occupation"),
#      # NEW: custom verify-token view which is not included in django-rest-passwordreset
#     url(r'^reset-password/verify-token/', api_view.CustomPasswordTokenVerificationView.as_view(), name='password_reset_verify_token'),
#     url(r'^reset-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
#     #url(r'^making_msg_read/$', api_view.making_msg_read, name="making_msg_read"),
#     url(r'^get_messages/$', api_view.get_messages, name="get_messages"),
#     url(r'^network_search/$', api_view.networking_search_result, name="network_search"),
#     
#     url(r'^wol_stream_fields/$', api_view.wol_stream_fields, name="wol_stream_fields"),
#     url(r'^wol_search_fields/(?P<type>[\w-]+)$', api_view.wol_search_fields, name="wol_search_fields"),
#     url(r'^search_major_autocomplete/(?P<type>[\w-]+)$', api_view.search_major_autocomplete, name="search_major_autocomplete"),
# #     url(r'^wol_shortlisted_dtl/$', api_view.wol_shortlisted_dtl, name="wol_shortlisted_dtl"),
# #     url(r'^explore_wol_shortlisted_edit/$', api_view.explore_wol_shortlisted_edit, name="explore_wol_shortlisted_edit"),
#     url(r'^wow_cluster_search/$', api_view.wow_cluster_search, name="wow_cluster_search"),
#     url(r'^get_occupation_search_key/(?P<type>[\w-]+)$', api_view.get_occupation_search_key, name="get_occupation_search_key"),
#     url(r'^get_pathway/$', api_view.get_pathway, name="get_pathway"),
#     url(r'^get_cluster_percentage/$', api_view.get_dashboard_percentage, name="get_cluster_percentage"),
#     url(r'^get_related_occ/(?P<occupation_id>[\w-]+)$', api_view.get_related_occupation_list, name="get_related_occ"),
#     url(r'^related_occ_summary_pdf/(?P<rel_occ>[\w-]+)$', api_view.related_occ_summary_pdf, name="related_occ_summary_pdf"),
#     url(r'^principal_dashboard/$', api_view.principal_dashboard, name="principal_dashboard"),
#     url(r'^district_edu_officer/$', api_view.district_edu_officer, name="district_edu_officer"),
#     url(r'^principal_users_list/$', api_view.principal_users_list, name="principal_users_list"),
#     url(r'^admin_profile_list/$', api_view.admin_profile_list, name="admin_profile_list"),
#     url(r'^gov_dash/$', api_view.gov_dash, name="gov_dash"),
#     url(r'^trans_mobile_login/(?P<user_token>[\w-]+)$', api_view.trans_mobile_login, name="trans_mobile_login"),

)



urlpatterns = format_suffix_patterns(urlpatterns)