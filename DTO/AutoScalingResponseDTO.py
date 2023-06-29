'''
Serilalization class for Autoscaling response
'''
from dataclasses import dataclass
from typing import Any, List, TypeVar, Type, cast, Callable
from datetime import datetime
from uuid import UUID
import dateutil.parser


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


@dataclass
class LaunchTemplate:
    launch_template_name: str
    version: int
    launch_template_id: str

    @staticmethod
    def from_dict(obj: Any) -> 'LaunchTemplate':
        assert isinstance(obj, dict)
        launch_template_name = from_str(obj.get("LaunchTemplateName"))
        version = int(from_str(obj.get("Version")))
        launch_template_id = from_str(obj.get("LaunchTemplateId"))
        return LaunchTemplate(launch_template_name, version, launch_template_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["LaunchTemplateName"] = from_str(self.launch_template_name)
        result["Version"] = from_str(str(self.version))
        result["LaunchTemplateId"] = from_str(self.launch_template_id)
        return result


@dataclass
class Instance:
    instance_id: str
    instance_type: str
    availability_zone: str
    health_status: str
    lifecycle_state: str
    protected_from_scale_in: bool
    launch_template: LaunchTemplate

    @staticmethod
    def from_dict(obj: Any) -> 'Instance':
        assert isinstance(obj, dict)
        instance_id = from_str(obj.get("InstanceId"))
        instance_type = from_str(obj.get("InstanceType"))
        availability_zone = from_str(obj.get("AvailabilityZone"))
        health_status = from_str(obj.get("HealthStatus"))
        lifecycle_state = from_str(obj.get("LifecycleState"))
        protected_from_scale_in = from_bool(obj.get("ProtectedFromScaleIn"))
        launch_template = LaunchTemplate.from_dict(obj.get("LaunchTemplate"))
        return Instance(instance_id, instance_type, availability_zone, health_status, lifecycle_state, protected_from_scale_in, launch_template)

    def to_dict(self) -> dict:
        result: dict = {}
        result["InstanceId"] = from_str(self.instance_id)
        result["InstanceType"] = from_str(self.instance_type)
        result["AvailabilityZone"] = from_str(self.availability_zone)
        result["HealthStatus"] = from_str(self.health_status)
        result["LifecycleState"] = from_str(self.lifecycle_state)
        result["ProtectedFromScaleIn"] = from_bool(self.protected_from_scale_in)
        result["LaunchTemplate"] = to_class(LaunchTemplate, self.launch_template)
        return result


@dataclass
class Tag:
    key: str
    propagate_at_launch: bool
    resource_id: str
    resource_type: str
    value: str

    @staticmethod
    def from_dict(obj: Any) -> 'Tag':
        assert isinstance(obj, dict)
        key = from_str(obj.get("Key"))
        propagate_at_launch = from_bool(obj.get("PropagateAtLaunch"))
        resource_id = from_str(obj.get("ResourceId"))
        resource_type = from_str(obj.get("ResourceType"))
        value = from_str(obj.get("Value"))
        return Tag(key, propagate_at_launch, resource_id, resource_type, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Key"] = from_str(self.key)
        result["PropagateAtLaunch"] = from_bool(self.propagate_at_launch)
        result["ResourceId"] = from_str(self.resource_id)
        result["ResourceType"] = from_str(self.resource_type)
        result["Value"] = from_str(self.value)
        return result


@dataclass
class AutoScalingGroup:
    auto_scaling_group_arn: str
    auto_scaling_group_name: str
    availability_zones: List[str]
    created_time: datetime
    default_cooldown: int
    desired_capacity: int
    enabled_metrics: List[Any]
    health_check_grace_period: int
    health_check_type: str
    instances: List[Instance]
    launch_template: LaunchTemplate
    load_balancer_names: List[Any]
    max_size: int
    min_size: int
    new_instances_protected_from_scale_in: bool
    service_linked_role_arn: str
    suspended_processes: List[Any]
    tags: List[Tag]
    target_group_ar_ns: List[Any]
    termination_policies: List[str]
    traffic_sources: List[Any]
    vpc_zone_identifier: str

    @staticmethod
    def from_dict(obj: Any) -> 'AutoScalingGroup':
        assert isinstance(obj, dict)
        auto_scaling_group_arn = from_str(obj.get("AutoScalingGroupARN"))
        auto_scaling_group_name = from_str(obj.get("AutoScalingGroupName"))
        availability_zones = from_list(from_str, obj.get("AvailabilityZones"))
        created_time = from_datetime(obj.get("CreatedTime"))
        default_cooldown = from_int(obj.get("DefaultCooldown"))
        desired_capacity = from_int(obj.get("DesiredCapacity"))
        enabled_metrics = from_list(lambda x: x, obj.get("EnabledMetrics"))
        health_check_grace_period = from_int(obj.get("HealthCheckGracePeriod"))
        health_check_type = from_str(obj.get("HealthCheckType"))
        instances = from_list(Instance.from_dict, obj.get("Instances"))
        launch_template = LaunchTemplate.from_dict(obj.get("LaunchTemplate"))
        load_balancer_names = from_list(lambda x: x, obj.get("LoadBalancerNames"))
        max_size = from_int(obj.get("MaxSize"))
        min_size = from_int(obj.get("MinSize"))
        new_instances_protected_from_scale_in = from_bool(obj.get("NewInstancesProtectedFromScaleIn"))
        service_linked_role_arn = from_str(obj.get("ServiceLinkedRoleARN"))
        suspended_processes = from_list(lambda x: x, obj.get("SuspendedProcesses"))
        tags = from_list(Tag.from_dict, obj.get("Tags"))
        target_group_ar_ns = from_list(lambda x: x, obj.get("TargetGroupARNs"))
        termination_policies = from_list(from_str, obj.get("TerminationPolicies"))
        traffic_sources = from_list(lambda x: x, obj.get("TrafficSources"))
        vpc_zone_identifier = from_str(obj.get("VPCZoneIdentifier"))
        return AutoScalingGroup(auto_scaling_group_arn, auto_scaling_group_name, availability_zones, created_time, default_cooldown, desired_capacity, enabled_metrics, health_check_grace_period, health_check_type, instances, launch_template, load_balancer_names, max_size, min_size, new_instances_protected_from_scale_in, service_linked_role_arn, suspended_processes, tags, target_group_ar_ns, termination_policies, traffic_sources, vpc_zone_identifier)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AutoScalingGroupARN"] = from_str(self.auto_scaling_group_arn)
        result["AutoScalingGroupName"] = from_str(self.auto_scaling_group_name)
        result["AvailabilityZones"] = from_list(from_str, self.availability_zones)
        result["CreatedTime"] = self.created_time.isoformat()
        result["DefaultCooldown"] = from_int(self.default_cooldown)
        result["DesiredCapacity"] = from_int(self.desired_capacity)
        result["EnabledMetrics"] = from_list(lambda x: x, self.enabled_metrics)
        result["HealthCheckGracePeriod"] = from_int(self.health_check_grace_period)
        result["HealthCheckType"] = from_str(self.health_check_type)
        result["Instances"] = from_list(lambda x: to_class(Instance, x), self.instances)
        result["LaunchTemplate"] = to_class(LaunchTemplate, self.launch_template)
        result["LoadBalancerNames"] = from_list(lambda x: x, self.load_balancer_names)
        result["MaxSize"] = from_int(self.max_size)
        result["MinSize"] = from_int(self.min_size)
        result["NewInstancesProtectedFromScaleIn"] = from_bool(self.new_instances_protected_from_scale_in)
        result["ServiceLinkedRoleARN"] = from_str(self.service_linked_role_arn)
        result["SuspendedProcesses"] = from_list(lambda x: x, self.suspended_processes)
        result["Tags"] = from_list(lambda x: to_class(Tag, x), self.tags)
        result["TargetGroupARNs"] = from_list(lambda x: x, self.target_group_ar_ns)
        result["TerminationPolicies"] = from_list(from_str, self.termination_policies)
        result["TrafficSources"] = from_list(lambda x: x, self.traffic_sources)
        result["VPCZoneIdentifier"] = from_str(self.vpc_zone_identifier)
        return result


@dataclass
class HTTPHeaders:
    content_length: int
    content_type: str
    date: str
    vary: str
    x_amzn_requestid: UUID

    @staticmethod
    def from_dict(obj: Any) -> 'HTTPHeaders':
        assert isinstance(obj, dict)
        content_length = int(from_str(obj.get("content-length")))
        content_type = from_str(obj.get("content-type"))
        date = from_str(obj.get("date"))
        vary = from_str(obj.get("vary"))
        x_amzn_requestid = UUID(obj.get("x-amzn-requestid"))
        return HTTPHeaders(content_length, content_type, date, vary, x_amzn_requestid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["content-length"] = from_str(str(self.content_length))
        result["content-type"] = from_str(self.content_type)
        result["date"] = from_str(self.date)
        result["vary"] = from_str(self.vary)
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
class AutoScalingResponseDTO:
    auto_scaling_groups: List[AutoScalingGroup]
    response_metadata: ResponseMetadata

    @staticmethod
    def from_dict(obj: Any) -> 'AutoScalingResponseDTO':
        assert isinstance(obj, dict)
        auto_scaling_groups = from_list(AutoScalingGroup.from_dict, obj.get("AutoScalingGroups"))
        response_metadata = ResponseMetadata.from_dict(obj.get("ResponseMetadata"))
        return AutoScalingResponseDTO(auto_scaling_groups, response_metadata)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AutoScalingGroups"] = from_list(lambda x: to_class(AutoScalingGroup, x), self.auto_scaling_groups)
        result["ResponseMetadata"] = to_class(ResponseMetadata, self.response_metadata)
        return result


def auto_scaling_response_dto_from_dict(s: Any) -> AutoScalingResponseDTO:
    return AutoScalingResponseDTO.from_dict(s)


def auto_scaling_response_dto_to_dict(x: AutoScalingResponseDTO) -> Any:
    return to_class(AutoScalingResponseDTO, x)


class AutoScalingResponseParser:
    ''' Main class to call the serializer'''
    def autoScalingResponseParsed(self,response_json):
        '''

        :param response_json: Json value of the Autoscaling response
        :return: Serialized class
        '''
        return auto_scaling_response_dto_from_dict(response_json)




