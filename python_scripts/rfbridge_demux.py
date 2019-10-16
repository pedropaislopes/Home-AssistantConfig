d = { '5BEC0A':['vidro_varchur'        ,'ON' ,'true'],
      '5BEC0E':['vidro_varchur'        ,'OFF','true'],
      '5E170A':['vidro_vargd'          ,'ON' ,'true'],
      '5E170E':['vidro_vargd'          ,'OFF','true'],
      '5A9D0A':['janela_escritorio'    ,'ON' ,'true'],
      '5A9D0E':['janela_escritorio'    ,'OFF','true'],
      '59C80A':['janela_quartolorena'  ,'ON' ,'true'],
      '59C80E':['janela_quartolorena'  ,'OFF','true'],
      '5C9C0A':['janela_suite'         ,'ON' ,'true'],
      '5C9C0E':['janela_suite'         ,'OFF','true'],
      '5C0A0A':['vidro_varpq'          ,'ON' ,'true'],
      '5C0A0E':['vidro_varpq'          ,'OFF','true'],
      '5D7C0A':['persiana_suite'       ,'ON' ,'true'],
      '5D7C0E':['persiana_suite'       ,'OFF','true'],
      '5DE40A':['persiana_quartolorena','ON' ,'true'],
      '5DE40E':['persiana_quartolorena','OFF','true']
    }

p = data.get('payload')

if p is not None:
  if p in d.keys():
    service_data = {'topic':'home/{}'.format(d[p][0]), 'payload':'{}'.format(d[p][1]), 'qos':0, 'retain':'{}'.format(d[p][2])}
  else:
    service_data = {'topic':'home/unknown', 'payload':'{}'.format(p), 'qos':0, 'retain':'false'}
    logger.warning('<rfbridge_demux> Received unknown RF command: {}'.format(p))
  hass.services.call('mqtt', 'publish', service_data, False)
