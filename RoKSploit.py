#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#ROKSploit
#RSF By NSK B3
import random, time, os
def banner():
    1st = '''
88""Yb  dP"Yb  88  dP          .dP"Y8 88""Yb 88      dP"Yb  88 888888     888888 88""Yb    db    8b    d8 888888 Yb        dP  dP"Yb  88""Yb 88  dP 
88__dP dP   Yb 88odP  ________ `Ybo." 88__dP 88     dP   Yb 88   88       88__   88__dP   dPYb   88b  d88 88__    Yb  db  dP  dP   Yb 88__dP 88odP  
88"Yb  Yb   dP 88"Yb  """""""" o.`Y8b 88"""  88  .o Yb   dP 88   88       88""   88"Yb   dP__Yb  88YbdP88 88""     YbdPYbdP   Yb   dP 88"Yb  88"Yb  
88  Yb  YbodP  88  Yb          8bodP' 88     88ood8  YbodP  88   88       88     88  Yb dP""""Yb 88 YY 88 888888    YP  YP     YbodP  88  Yb 88  Yb 
'''
    2nd = '''
 ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄    ▄         ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄           ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄▄       ▄▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄         ▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄ ▄    ▄ 
▐░░░░░░░░░░░▐░░░░░░░░░░░▐░▌  ▐░▌       ▐░░░░░░░░░░░▐░░░░░░░░░░░▐░▌         ▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░▌     ▐░░▐░░░░░░░░░░░▐░▌       ▐░▐░░░░░░░░░░░▐░░░░░░░░░░░▐░▌  ▐░▌
▐░█▀▀▀▀▀▀▀█░▐░█▀▀▀▀▀▀▀█░▐░▌ ▐░▌        ▐░█▀▀▀▀▀▀▀▀▀▐░█▀▀▀▀▀▀▀█░▐░▌         ▐░█▀▀▀▀▀▀▀█░▌▀▀▀▀█░█▀▀▀▀ ▀▀▀▀█░█▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀▐░█▀▀▀▀▀▀▀█░▐░█▀▀▀▀▀▀▀█░▐░▌░▌   ▐░▐░▐░█▀▀▀▀▀▀▀▀▀▐░▌       ▐░▐░█▀▀▀▀▀▀▀█░▐░█▀▀▀▀▀▀▀█░▐░▌ ▐░▌ 
▐░▌       ▐░▐░▌       ▐░▐░▌▐░▌         ▐░▌         ▐░▌       ▐░▐░▌         ▐░▌       ▐░▌    ▐░▌         ▐░▌          ▐░▌         ▐░▌       ▐░▐░▌       ▐░▐░▌▐░▌ ▐░▌▐░▐░▌         ▐░▌       ▐░▐░▌       ▐░▐░▌       ▐░▐░▌▐░▌  
▐░█▄▄▄▄▄▄▄█░▐░▌       ▐░▐░▌░▄▄▄▄▄▄▄▄▄▄▄▐░█▄▄▄▄▄▄▄▄▄▐░█▄▄▄▄▄▄▄█░▐░▌         ▐░▌       ▐░▌    ▐░▌         ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄▐░█▄▄▄▄▄▄▄█░▐░█▄▄▄▄▄▄▄█░▐░▌ ▐░▐░▌ ▐░▐░█▄▄▄▄▄▄▄▄▄▐░▌   ▄   ▐░▐░▌       ▐░▐░█▄▄▄▄▄▄▄█░▐░▌░▌   
▐░░░░░░░░░░░▐░▌       ▐░▐░░▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░░░░░░░░░░▐░▌         ▐░▌       ▐░▌    ▐░▌         ▐░▌          ▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░░░░░░░░░░▐░▌  ▐░▌  ▐░▐░░░░░░░░░░░▐░▌  ▐░▌  ▐░▐░▌       ▐░▐░░░░░░░░░░░▐░░▌    
▐░█▀▀▀▀█░█▀▀▐░▌       ▐░▐░▌░▀▀▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀█░▐░█▀▀▀▀▀▀▀▀▀▐░▌         ▐░▌       ▐░▌    ▐░▌         ▐░▌          ▐░█▀▀▀▀▀▀▀▀▀▐░█▀▀▀▀█░█▀▀▐░█▀▀▀▀▀▀▀█░▐░▌   ▀   ▐░▐░█▀▀▀▀▀▀▀▀▀▐░▌ ▐░▌░▌ ▐░▐░▌       ▐░▐░█▀▀▀▀█░█▀▀▐░▌░▌   
▐░▌     ▐░▌ ▐░▌       ▐░▐░▌▐░▌                   ▐░▐░▌         ▐░▌         ▐░▌       ▐░▌    ▐░▌         ▐░▌          ▐░▌         ▐░▌     ▐░▌ ▐░▌       ▐░▐░▌       ▐░▐░▌         ▐░▌▐░▌ ▐░▌▐░▐░▌       ▐░▐░▌     ▐░▌ ▐░▌▐░▌  
▐░▌      ▐░▌▐░█▄▄▄▄▄▄▄█░▐░▌ ▐░▌         ▄▄▄▄▄▄▄▄▄█░▐░▌         ▐░█▄▄▄▄▄▄▄▄▄▐░█▄▄▄▄▄▄▄█░▌▄▄▄▄█░█▄▄▄▄     ▐░▌          ▐░▌         ▐░▌      ▐░▌▐░▌       ▐░▐░▌       ▐░▐░█▄▄▄▄▄▄▄▄▄▐░▌░▌   ▐░▐░▐░█▄▄▄▄▄▄▄█░▐░▌      ▐░▌▐░▌ ▐░▌ 
▐░▌       ▐░▐░░░░░░░░░░░▐░▌  ▐░▌       ▐░░░░░░░░░░░▐░▌         ▐░░░░░░░░░░░▐░░░░░░░░░░░▐░░░░░░░░░░░▌    ▐░▌          ▐░▌         ▐░▌       ▐░▐░▌       ▐░▐░▌       ▐░▐░░░░░░░░░░░▐░░▌     ▐░░▐░░░░░░░░░░░▐░▌       ▐░▐░▌  ▐░▌
 ▀         ▀ ▀▀▀▀▀▀▀▀▀▀▀ ▀    ▀         ▀▀▀▀▀▀▀▀▀▀▀ ▀           ▀▀▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀▀▀      ▀            ▀           ▀         ▀ ▀         ▀ ▀         ▀ ▀▀▀▀▀▀▀▀▀▀▀ ▀▀       ▀▀ ▀▀▀▀▀▀▀▀▀▀▀ ▀         ▀ ▀    ▀ 
                                                                                                                                                                                                             
'''
    3rd = '''
      :::::::::   ::::::::  :::    :::                ::::::::  :::::::::  :::        :::::::: ::::::::::: :::::::::::           :::::::::: :::::::::      :::       :::   :::   :::::::::: :::       :::  ::::::::  :::::::::  :::    ::: 
     :+:    :+: :+:    :+: :+:   :+:                :+:    :+: :+:    :+: :+:       :+:    :+:    :+:         :+:               :+:        :+:    :+:   :+: :+:    :+:+: :+:+:  :+:        :+:       :+: :+:    :+: :+:    :+: :+:   :+:   
    +:+    +:+ +:+    +:+ +:+  +:+                 +:+        +:+    +:+ +:+       +:+    +:+    +:+         +:+               +:+        +:+    +:+  +:+   +:+  +:+ +:+:+ +:+ +:+        +:+       +:+ +:+    +:+ +:+    +:+ +:+  +:+     
   +#++:++#:  +#+    +:+ +#++:++    +#++:++#++:++ +#++:++#++ +#++:++#+  +#+       +#+    +:+    +#+         +#+               :#::+::#   +#++:++#:  +#++:++#++: +#+  +:+  +#+ +#++:++#   +#+  +:+  +#+ +#+    +:+ +#++:++#:  +#++:++       
  +#+    +#+ +#+    +#+ +#+  +#+                        +#+ +#+        +#+       +#+    +#+    +#+         +#+               +#+        +#+    +#+ +#+     +#+ +#+       +#+ +#+        +#+ +#+#+ +#+ +#+    +#+ +#+    +#+ +#+  +#+       
 #+#    #+# #+#    #+# #+#   #+#                #+#    #+# #+#        #+#       #+#    #+#    #+#         #+#               #+#        #+#    #+# #+#     #+# #+#       #+# #+#         #+#+# #+#+#  #+#    #+# #+#    #+# #+#   #+#       
###    ###  ########  ###    ###                ########  ###        ########## ######## ###########     ###               ###        ###    ### ###     ### ###       ### ##########   ###   ###    ########  ###    ### ###    ###       
'''
    arts = [1st, 2nd, 3rd]
    print random.choice(arts)
