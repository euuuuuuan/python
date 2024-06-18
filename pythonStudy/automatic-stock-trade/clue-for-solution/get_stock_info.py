# 이번엔 본격적으로 API를 연동하기 전에 주식 현재가를 받아 오는 함수만 먼저 작성해 볼게요. 앞에서 접근 토큰을 가져오는 함수를 작성해 봤던 거 기억나시나요?
#
#  get_token.py
#
#
# import requests
#
# BASE_URL = "https://openapivts.koreainvestment.com:29443"
# APPKEY = "..."
# APPSECRET = "..."
#
# url = f"{BASE_URL}/oauth2/tokenP"
# headers = {
#     "Content-Type": "application/json"
# }
# body = {
#     "grant_type": "client_credentials",
#     "appkey": APPKEY,
#     "appsecret": APPSECRET
# }
# res = requests.post(url, headers=headers, json=body)
# try:
#     data = res.json()
#     print(data)
# except Exception as e:
#     print(e)
# 이 함수로 일단 접근 토큰을 발급을 받고 접근 토큰 값을 잘 적어 두겠습니다. 파이썬 코드에서 자동으로 접근 토큰을 관리하면 좋겠지만, 일단은 단순하게 ACCESS_TOKEN이라는 변수 값으로 정의해 놓고 쓰는 걸로 구현할게요.
#
# API 문서에서 리퀘스트 살펴보기
# API 문서에서 주식 현재가 시세 항목을 살펴보면 다음과 같습니다.
#
# xj7cx0fan-image.png
#
# 보낼 리퀘스트의 형식을 정리해 볼게요. 우선 메소드는 GET이고요, 주소를 보면 /uapi/domestic-stock/v1/quotations/inquire-price로 보내야 할 거 같네요.
#
# 필요한 헤더는 다음과 같이 정리할 수 있겠습니다.
#
#
# authorization: Bearer <접근 토큰 값>
# appkey: <app key 값>
# appsecret: <app secret 값>
# tr_id: FHKST01010100
# 쿼리 파라미터는 아래와 같이 정리할 수 있어요.
#
#
# FID_COND_MRKT_DIV_CODE: J
# FID_INPUT_ISCD: 종목 번호
# 파이썬 코드 작성해 보기
# 이걸 가지고 현재가를 조회하는 파이썬 함수를 작성해 볼게요. api_test.py라는 파일을 임시로 만들고 API만 테스트해 봅시다.
#
# fetch_current_price()라는 함수를 구현할 건데요. 조회할 종목 코드를 code라는 파라미터로 받아서 조회하도록 해 보겠습니다. 헤더 값은 headers라는 사전으로 만들었고요, 쿼리 파라미터는 params라는 사전으로 만들어서 requests.request() 함수에 아규먼트로 전달했습니다. 삼성전자(005930)로 한 번 조회를 해 보면 아래와 같이 출력됩니다.
#
#  api_test.py
#
#
# import requests
#
# BASE_URL = "https://openapivts.koreainvestment.com:29443"
# APPKEY="..."
# APPSECRET="..."
#
# ACCESS_TOKEN = "..."
#
# def fetch_current_price(code):
#     url = f"{BASE_URL}/uapi/domestic-stock/v1/quotations/inquire-price"
#     headers = {
#         "authorization": f"Bearer {ACCESS_TOKEN}",
#         "appkey": APPKEY,
#         "appsecret": APPSECRET,
#         "tr_id": "FHKST01010100"
#     }
#     params = {
#         "FID_COND_MRKT_DIV_CODE": "J",
#         "FID_INPUT_ISCD": code
#     }
#     try:
#         res = requests.get(url, headers=headers, params=params)
#         data = res.json()
#         return data
#     except Exception as e:
#         print(e)
#         return None
#
# print(fetch_current_price("005930"))
#
#
# {'output': {'iscd_stat_cls_code': '55', 'marg_rate': '20.00', 'rprs_mrkt_kor_name': 'KOSPI200', 'bstp_kor_isnm': '전기.전자', 'temp_stop_yn': 'N', 'oprc_rang_cont_yn': 'N', 'clpr_rang_cont_yn': 'N', 'crdt_able_yn': 'Y', 'grmn_rate_cls_code': '40', 'elw_pblc_yn': 'Y', 'stck_prpr': '76300', 'prdy_vrss': '-2300', 'prdy_vrss_sign': '5', 'prdy_ctrt': '-2.93', 'acml_tr_pbmn': '1195063612340', 'acml_vol': '15549134', 'prdy_vrss_vol_rate': '70.15', 'stck_oprc': '77300', 'stck_hgpr': '77500', 'stck_lwpr': '76300', 'stck_mxpr': '102100', 'stck_llam': '55100', 'stck_sdpr': '78600', 'wghn_avrg_stck_prc': '76859.74', 'hts_frgn_ehrt': '55.86', 'frgn_ntby_qty': '-636056', 'pgtr_ntby_qty': '-1684066', 'pvt_scnd_dmrs_prc': '79800', 'pvt_frst_dmrs_prc': '79200', 'pvt_pont_val': '78200', 'pvt_frst_dmsp_prc': '77600', 'pvt_scnd_dmsp_prc': '76600', 'dmrs_val': '79500', 'dmsp_val': '77900', 'cpfn': '7780', 'rstc_wdth_prc': '23500', 'stck_fcam': '100', 'stck_sspr': '62880', 'aspr_unit': '100', 'hts_deal_qty_unit_val': '1', 'lstn_stcn': '5969782550', 'hts_avls': '4554944', 'per': '35.80', 'pbr': '1.47', 'stac_month': '12', 'vol_tnrt': '0.26', 'eps': '2131.00', 'bps': '52002.00', 'd250_hgpr': '86000', 'd250_hgpr_date': '20240408', 'd250_hgpr_vrss_prpr_rate': '-11.28', 'd250_lwpr': '63300', 'd250_lwpr_date': '20230426', 'd250_lwpr_vrss_prpr_rate': '20.54', 'stck_dryy_hgpr': '86000', 'dryy_hgpr_vrss_prpr_rate': '-11.28', 'dryy_hgpr_date': '20240408', 'stck_dryy_lwpr': '70700', 'dryy_lwpr_vrss_prpr_rate': '7.92', 'dryy_lwpr_date': '20240118', 'w52_hgpr': '86000', 'w52_hgpr_vrss_prpr_ctrt': '-11.28', 'w52_hgpr_date': '20240408', 'w52_lwpr': '63300', 'w52_lwpr_vrss_prpr_ctrt': '20.54', 'w52_lwpr_date': '20230426', 'whol_loan_rmnd_rate': '0.13', 'ssts_yn': 'N', 'stck_shrn_iscd': '005930', 'fcam_cnnm': '100', 'cpfn_cnnm': '7,780 억', 'frgn_hldn_qty': '3334761646', 'vi_cls_code': 'N', 'ovtm_vi_cls_code': 'N', 'last_ssts_cntg_qty': '44759', 'invt_caful_yn': 'N', 'mrkt_warn_cls_code': '00', 'short_over_yn': 'N', 'sltr_yn': 'N'}, 'rt_cd': '0', 'msg_cd': 'MCA00000', 'msg1': '정상처리 되었습니다.'}
# 2024년 4월 25일 장이 마감된 시점에서 삼성전자의 현재가는 76,300원인데요. 이제 이 가격을 잘 받아 왔는지 한번 확인해 볼게요.
#
# API 문서에서 리스폰스 살펴보기
# 다시 API 문서를 살펴보면 우리가 원하는 주식 현재가는 output이라는 속성 아래에 stck_prpr이라는 속성에 들어 있는 것 같습니다.
#
# 13hyprbml-image.png
#
# 파이썬 코드로 표현한다면, 바디 값이 data라는 변수에 저장되어 있을 때 data["output"]["stck_prpr"]이라고 표현할 수 있겠네요.
#
# 함수 리턴 값 수정해 보기
# 우리한테 필요한 값인 주식 현재가 값만 함수에서 리턴하고, 이 값이 없으면 None을 리턴하는 식으로 코드를 바꿔 볼게요. 이때 리턴하는 값은 가격이니까, 정수형이 되도록 int() 함수를 사용해서 리턴해 주도록 하겠습니다.
#
# 이 코드를 실행하면 2024년 4월 25일 기준으로 삼성전자 종가인 76300이란 값이 잘 출력되네요. 여러분이 코드를 실행하는 시점에는 다른 값이 출력될 거예요.
#
#  api_test.py
#
#
# import requests
#
# BASE_URL = "https://openapivts.koreainvestment.com:29443"
# APPKEY="..."
# APPSECRET="..."
#
# ACCESS_TOKEN = "..."
#
# def fetch_current_price(code):
#     url = f"{BASE_URL}/uapi/domestic-stock/v1/quotations/inquire-price"
#     headers = {
#         "authorization": f"Bearer {ACCESS_TOKEN}",
#         "appkey": APPKEY,
#         "appsecret": APPSECRET,
#         "tr_id": "FHKST01010100"
#     }
#     params = {
#         "FID_COND_MRKT_DIV_CODE": "J",
#         "FID_INPUT_ISCD": code
#     }
#     res = requests.get(url, headers=headers, params=params)
#     try:
#         data = res.json()
#         return int(data["output"]["stck_prpr"])
#     except Exception as e:
#         print(e)
#         return None
#
# print(fetch_current_price("005930"))
#
# 76300
# 다음 레슨에서는 이 코드를 활용해서 자동 매매 코드의 틀을 한 번 만들어 보겠습니다.