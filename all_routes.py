# auth
auth_login = '/auth/login'

# smtp servers
smtp_create_server = '/smtp/create'
smtp_all_servers = '/all/smtp/{uuid}'
smtp_update = '/update/smtp/{smtp_id}'
smtp_delete = '/delete/smtp/{server_id}'
smtp_get = '/smtp/{server_id}'

# Templates
template_create = '/create/template'
template_edit = '/update/template/{template_id}'
template_get = '/template/{template_id}'
template_delete = '/delete/template/{template_id}'
template_all = '/all/templates'

# subscriptions
subscriptions_create = '/create/subscription'
subscription_unsubscribe = '/unsubscribe'
subscription_all = '/all/subscription'

# campaign
campaign_create = '/create/campaign'
campaign_all = '/all/campaigns'

# analytics
analytics_yearly_campaigns = '/analytics/yearly/campaigns/{year}'
analytics_yearly_subscriptions = '/analytics/yearly/subscriptions/{year}'
