def template_layout(content):
    return F""" 
      <body style="max-width: 700px; width:100%; margin: 0; padding-top: 20pxpx; -webkit-text-size-adjust: 100%;background-color: #F1F1F1; color: #000000">
      {content}
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
                Email template built by <a style="text-decoration: none; color: #919293;" href="https://fullsphere.co.uk"><u>Subscribe to my email list</u></a>
              </p>

            </td>
          </tr>
        </tbody>
      </table>
      <!-- End unsubscribe section -->
      </body>
    """