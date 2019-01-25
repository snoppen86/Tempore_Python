import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services.response_service import main_response_handler
from .services.database_inserter import dose_user_exist_in_db, upsert_user_info

log = logging.getLogger(__file__)


@api_view(['POST'])
def update_user_request(request):
    try:
        data = request.data
        person = data['Person']
        find_user = dose_user_exist_in_db(person['Email'])
        if find_user is True:
            upsert_user_info(person)
            Response({'massage': "User is updated"})
    except:
        log.warning("fail")
