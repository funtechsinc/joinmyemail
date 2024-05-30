from functions.config import website_uri
from functions.config import api_uri


def template_layout(content, memoji, company, category, email=None, campaign_id=None):
    tracking_pexel = f"""<img src = "{api_uri}/tracking-pixel?email={email}&campaign={campaign_id}" 
    width = "1"
    height = "1"
    style = "display:none;"
    alt = "" />""" if campaign_id is not None else ''
    content: str = content.replace('<img', ''' <img width='100%' ''')
    return F""" 
      <body style="font-size: 16px;line-height: 1.4; max-width: 700px; width:100%; margin: 0 auto; padding:20px 30px;border-radius:20px; -webkit-text-size-adjust: 100%;background-color: #FAFAFA; color: #000000">
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
   <div style="margin-top:10px;margin-bottom:10px;border-bottom:0.1rem solid #404040;"></div>
     {content}
    <footer style="margin:20px 0;">
        <!-- Start unsubscribe section -->
      <table align="center" style="text-align: center; vertical-align: top; width: 600px; max-width: 600px;" width="600">
        <tbody>
          <tr>
            <td style="width: 596px; vertical-align: top; padding-left: 30px; padding-right: 30px; padding-top: 30px; padding-bottom: 30px;" width="596">
              <p style="font-size: 12px; line-height: 12px; font-family: 'Helvetica', Arial, sans-serif; font-weight: normal; text-decoration: none; color: #000000;">
                Not wanting to receive these emails?
              </p>

              <p style="font-size: 12px; line-height: 12px; font-family: 'Helvetica', Arial, sans-serif; font-weight: normal; text-decoration: none; color: #000000;">
                You can <a style="text-decoration: underline; color: #000000;" href="insert-unsubscribe-link-here"><u>unsubscribe here</u></a>
              </p>

              <p style="font-size: 12px; line-height: 12px; font-family: 'Helvetica', Arial, sans-serif; font-weight: normal; text-decoration: none; color: #919293; margin-top: 30px;">
                Email template built by <a style="text-decoration: none; color: #919293;" href="#"><u>Subscribe to my email list</u></a>
              </p>

            </td>
          </tr>
        </tbody>
      </table>
      <!-- End unsubscribe section -->
   </footer>
     <!-- Tracking Pixel -->
     {tracking_pexel}
     
      </body>
    """
