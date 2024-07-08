from functions.config import website_uri
from functions.config import api_uri


def template_layout(content, memoji, company, category, email=None, campaign_id=None, hash_token=None):
    tracking_pexel = f"""<img src = "{api_uri}/tracking-pixel?email={email}&campaign={campaign_id}" 
    width = "1"
    height = "1"
    style = "display:none;"
    alt = "" />""" if campaign_id is not None else ''
    content: str = content.replace('<img', ''' <img style="max-width:100%; height:auto;" ''')
    unsub = F"""
        <p style=" font-family: 'Helvetica', Arial, sans-serif; font-weight: normal; text-decoration: none; color: #404040;">
                Not wanting to receive these emails?
              </p>
              <p>
               <a  style="font-family: 'Helvetica', Arial, sans-serif; color: #6366f1;" href="{website_uri}/unsubscribe/{hash_token}">
                 <b><u>unsubscribe here</u></b>
                 </a>
                </p>
             """ if campaign_id is not None else ''

    return F""" 
      <body style="font-size: 16px;line-height: 1.4; max-width: 700px; width:100%; margin: 0 auto; padding:20px 30px;border-radius:20px; -webkit-text-size-adjust: 100%;">
      <div style="text-align: center; margin-bottom:20px;">
        <img src="{website_uri}{memoji}"
             width="100px"
             height='100px'
             />
        <br />
        <div>
          <b>{company}</b>
        </div>
             <div>
               <div style="font-size:14px;">{category}</div>
        </div>
         
     </div>
   <div style="margin-top:10px;margin-bottom:10px;border-bottom:0.1rem solid #dddddd;"></div>
     {content}
    <div style="margin-top:20px;margin-bottom:10px;border-bottom:0.1rem solid #dddddd;"></div>
    <div align="center" style="text-align: center; vertical-align: top;" >
        <!-- Start unsubscribe section -->
            {unsub}
              <p >
               <a style="text-decoration: none; color: #919293;" href="#">
                 <img src='{website_uri}/logo.png' width='200px'/>
               </a>
              </p>
      <!-- End unsubscribe section -->
   </div>
     <!-- Tracking Pixel -->
     {tracking_pexel}
     
      </body>
    """
