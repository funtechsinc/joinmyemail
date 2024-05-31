# auth
auth_login = '/auth/login'
auth_register = '/auth/register'
auth_create_user_handle = '/user/handle/{uuid}'
auth_create_welcome_message = '/auth/welcome/{uuid}'
auth_update = '/auth/update/{uuid}'
auth_get_user = '/user/{uuid}'
auth_get_user_with_handle = '/user/handle/{handle}'

# smtp servers
smtp_create_server = '/smtp/create/{uuid}'
smtp_all_servers = '/all/smtp/{uuid}'
smtp_update = '/update/smtp/{smtp_id}'
smtp_delete = '/delete/smtp/{server_id}'
smtp_get = '/smtp/{server_id}'

# Templates
template_create = '/create/template/{uuid}'
template_edit = '/update/template/{template_id}'
template_get = '/template/{template_id}'
template_delete = '/delete/template/{template_id}'
template_all = '/all/templates/{uuid}'

# subscriptions
subscriptions_create = '/create/subscription/{handle}'
subscription_unsubscribe = '/unsubscribe'
subscription_all = '/all/subscription/{uuid}'

# campaign
campaign_create = '/create/campaign/{uuid}'
campaign_all = '/all/campaigns/{uuid}'
campaign_delete = '/delete/campaign/{campaign_id}'
campaign_edit = '/edit/campaign/{campaign_id}'

# analytics
analytics_yearly_campaigns = '/analytics/yearly/campaigns/{year}/{uuid}'
analytics_yearly_subscriptions = '/analytics/yearly/subscriptions/{year}/{uuid}'

# opening emails
campaign_opens = '/campaign/opens/{campaign_id}'
