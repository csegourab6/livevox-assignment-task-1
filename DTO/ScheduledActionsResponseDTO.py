'''
Serilalization class for Describe Scheduled Actions response
'''
from dataclasses import dataclass
from uuid import UUID
from typing import Any, List, TypeVar, Type, cast, Callable
from datetime import datetime
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class HTTPHeaders:
    content_length: int
    content_type: str
    date: str
    x_amzn_requestid: UUID

    @staticmethod
    def from_dict(obj: Any) -> 'HTTPHeaders':
        assert isinstance(obj, dict)
        content_length = int(from_str(obj.get("content-length")))
        content_type = from_str(obj.get("content-type"))
        date = from_str(obj.get("date"))
        x_amzn_requestid = UUID(obj.get("x-amzn-requestid"))
        return HTTPHeaders(content_length, content_type, date, x_amzn_requestid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["content-length"] = from_str(str(self.content_length))
        result["content-type"] = from_str(self.content_type)
        result["date"] = from_str(self.date)
        result["x-amzn-requestid"] = str(self.x_amzn_requestid)
        return result


@dataclass
class ResponseMetadata:
    http_headers: HTTPHeaders
    http_status_code: int
    request_id: UUID
    retry_attempts: int

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        http_headers = HTTPHeaders.from_dict(obj.get("HTTPHeaders"))
        http_status_code = from_int(obj.get("HTTPStatusCode"))
        request_id = UUID(obj.get("RequestId"))
        retry_attempts = from_int(obj.get("RetryAttempts"))
        return ResponseMetadata(http_headers, http_status_code, request_id, retry_attempts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["HTTPHeaders"] = to_class(HTTPHeaders, self.http_headers)
        result["HTTPStatusCode"] = from_int(self.http_status_code)
        result["RequestId"] = str(self.request_id)
        result["RetryAttempts"] = from_int(self.retry_attempts)
        return result


@dataclass
class ScheduledUpdateGroupAction:
    auto_scaling_group_name: str
    desired_capacity: int
    max_size: int
    min_size: int
    recurrence: str
    scheduled_action_arn: str
    scheduled_action_name: str
    start_time: datetime
    time: datetime
    time_zone: str

    @staticmethod
    def from_dict(obj: Any) -> 'ScheduledUpdateGroupAction':
        assert isinstance(obj, dict)
        auto_scaling_group_name = from_str(obj.get("AutoScalingGroupName"))
        desired_capacity = from_int(obj.get("DesiredCapacity"))
        max_size = from_int(obj.get("MaxSize"))
        min_size = from_int(obj.get("MinSize"))
        recurrence = from_str(obj.get("Recurrence"))
        scheduled_action_arn = from_str(obj.get("ScheduledActionARN"))
        scheduled_action_name = from_str(obj.get("ScheduledActionName"))
        start_time = from_datetime(obj.get("StartTime"))
        time = from_datetime(obj.get("Time"))
        time_zone = from_str(obj.get("TimeZone"))
        return ScheduledUpdateGroupAction(auto_scaling_group_name, desired_capacity, max_size, min_size, recurrence, scheduled_action_arn, scheduled_action_name, start_time, time, time_zone)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AutoScalingGroupName"] = from_str(self.auto_scaling_group_name)
        result["DesiredCapacity"] = from_int(self.desired_capacity)
        result["MaxSize"] = from_int(self.max_size)
        result["MinSize"] = from_int(self.min_size)
        result["Recurrence"] = from_str(self.recurrence)
        result["ScheduledActionARN"] = from_str(self.scheduled_action_arn)
        result["ScheduledActionName"] = from_str(self.scheduled_action_name)
        result["StartTime"] = self.start_time.isoformat()
        result["Time"] = self.time.isoformat()
        result["TimeZone"] = from_str(self.time_zone)
        return result


@dataclass
class ScheduledActionResponseResponseDTO:
    response_metadata: ResponseMetadata
    scheduled_update_group_actions: List[ScheduledUpdateGroupAction]

    @staticmethod
    def from_dict(obj: Any) -> 'ScheduledActionResponseResponseDTO':
        assert isinstance(obj, dict)
        response_metadata = ResponseMetadata.from_dict(obj.get("ResponseMetadata"))
        scheduled_update_group_actions = from_list(ScheduledUpdateGroupAction.from_dict, obj.get("ScheduledUpdateGroupActions"))
        return ScheduledActionResponseResponseDTO(response_metadata, scheduled_update_group_actions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ResponseMetadata"] = to_class(ResponseMetadata, self.response_metadata)
        result["ScheduledUpdateGroupActions"] = from_list(lambda x: to_class(ScheduledUpdateGroupAction, x), self.scheduled_update_group_actions)
        return result


def scheduled_action_response_response_dto_from_dict(s: Any) -> ScheduledActionResponseResponseDTO:
    return ScheduledActionResponseResponseDTO.from_dict(s)


def scheduled_action_response_response_dto_to_dict(x: ScheduledActionResponseResponseDTO) -> Any:
    return to_class(ScheduledActionResponseResponseDTO, x)

class ScheduledActionsResponseParser:
    '''Main Serilalization class for Describe Scheduled Actions response'''
    def describeScheduledActionsResponseParsed(self,response_json):
        '''

        :param response_json: response in json from describe scheduled response
        :return: Serialized class of the response
        '''
        return scheduled_action_response_response_dto_from_dict(response_json)