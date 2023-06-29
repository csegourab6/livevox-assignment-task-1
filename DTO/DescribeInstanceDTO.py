'''
Serilalization class for Describe Instance response
'''
from dataclasses import dataclass
from datetime import datetime
from typing import Any, List, TypeVar, Type, cast, Callable
from uuid import UUID
import dateutil.parser


T = TypeVar("T")


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class Ebs:
    attach_time: datetime
    delete_on_termination: bool
    status: str
    volume_id: str

    @staticmethod
    def from_dict(obj: Any) -> 'Ebs':
        assert isinstance(obj, dict)
        attach_time = from_datetime(obj.get("AttachTime"))
        delete_on_termination = from_bool(obj.get("DeleteOnTermination"))
        status = from_str(obj.get("Status"))
        volume_id = from_str(obj.get("VolumeId"))
        return Ebs(attach_time, delete_on_termination, status, volume_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AttachTime"] = self.attach_time.isoformat()
        result["DeleteOnTermination"] = from_bool(self.delete_on_termination)
        result["Status"] = from_str(self.status)
        result["VolumeId"] = from_str(self.volume_id)
        return result


@dataclass
class BlockDeviceMapping:
    device_name: str
    ebs: Ebs

    @staticmethod
    def from_dict(obj: Any) -> 'BlockDeviceMapping':
        assert isinstance(obj, dict)
        device_name = from_str(obj.get("DeviceName"))
        ebs = Ebs.from_dict(obj.get("Ebs"))
        return BlockDeviceMapping(device_name, ebs)

    def to_dict(self) -> dict:
        result: dict = {}
        result["DeviceName"] = from_str(self.device_name)
        result["Ebs"] = to_class(Ebs, self.ebs)
        return result


@dataclass
class CapacityReservationSpecification:
    capacity_reservation_preference: str

    @staticmethod
    def from_dict(obj: Any) -> 'CapacityReservationSpecification':
        assert isinstance(obj, dict)
        capacity_reservation_preference = from_str(obj.get("CapacityReservationPreference"))
        return CapacityReservationSpecification(capacity_reservation_preference)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CapacityReservationPreference"] = from_str(self.capacity_reservation_preference)
        return result


@dataclass
class CPUOptions:
    core_count: int
    threads_per_core: int

    @staticmethod
    def from_dict(obj: Any) -> 'CPUOptions':
        assert isinstance(obj, dict)
        core_count = from_int(obj.get("CoreCount"))
        threads_per_core = from_int(obj.get("ThreadsPerCore"))
        return CPUOptions(core_count, threads_per_core)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CoreCount"] = from_int(self.core_count)
        result["ThreadsPerCore"] = from_int(self.threads_per_core)
        return result


@dataclass
class EnclaveOptions:
    enabled: bool

    @staticmethod
    def from_dict(obj: Any) -> 'EnclaveOptions':
        assert isinstance(obj, dict)
        enabled = from_bool(obj.get("Enabled"))
        return EnclaveOptions(enabled)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Enabled"] = from_bool(self.enabled)
        return result


@dataclass
class HibernationOptions:
    configured: bool

    @staticmethod
    def from_dict(obj: Any) -> 'HibernationOptions':
        assert isinstance(obj, dict)
        configured = from_bool(obj.get("Configured"))
        return HibernationOptions(configured)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Configured"] = from_bool(self.configured)
        return result


@dataclass
class MaintenanceOptions:
    auto_recovery: str

    @staticmethod
    def from_dict(obj: Any) -> 'MaintenanceOptions':
        assert isinstance(obj, dict)
        auto_recovery = from_str(obj.get("AutoRecovery"))
        return MaintenanceOptions(auto_recovery)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AutoRecovery"] = from_str(self.auto_recovery)
        return result


@dataclass
class MetadataOptions:
    http_endpoint: str
    http_protocol_ipv6: str
    http_put_response_hop_limit: int
    http_tokens: str
    instance_metadata_tags: str
    state: str

    @staticmethod
    def from_dict(obj: Any) -> 'MetadataOptions':
        assert isinstance(obj, dict)
        http_endpoint = from_str(obj.get("HttpEndpoint"))
        http_protocol_ipv6 = from_str(obj.get("HttpProtocolIpv6"))
        http_put_response_hop_limit = from_int(obj.get("HttpPutResponseHopLimit"))
        http_tokens = from_str(obj.get("HttpTokens"))
        instance_metadata_tags = from_str(obj.get("InstanceMetadataTags"))
        state = from_str(obj.get("State"))
        return MetadataOptions(http_endpoint, http_protocol_ipv6, http_put_response_hop_limit, http_tokens, instance_metadata_tags, state)

    def to_dict(self) -> dict:
        result: dict = {}
        result["HttpEndpoint"] = from_str(self.http_endpoint)
        result["HttpProtocolIpv6"] = from_str(self.http_protocol_ipv6)
        result["HttpPutResponseHopLimit"] = from_int(self.http_put_response_hop_limit)
        result["HttpTokens"] = from_str(self.http_tokens)
        result["InstanceMetadataTags"] = from_str(self.instance_metadata_tags)
        result["State"] = from_str(self.state)
        return result


@dataclass
class Monitoring:
    state: str

    @staticmethod
    def from_dict(obj: Any) -> 'Monitoring':
        assert isinstance(obj, dict)
        state = from_str(obj.get("State"))
        return Monitoring(state)

    def to_dict(self) -> dict:
        result: dict = {}
        result["State"] = from_str(self.state)
        return result


@dataclass
class Attachment:
    attach_time: datetime
    attachment_id: str
    delete_on_termination: bool
    device_index: int
    network_card_index: int
    status: str

    @staticmethod
    def from_dict(obj: Any) -> 'Attachment':
        assert isinstance(obj, dict)
        attach_time = from_datetime(obj.get("AttachTime"))
        attachment_id = from_str(obj.get("AttachmentId"))
        delete_on_termination = from_bool(obj.get("DeleteOnTermination"))
        device_index = from_int(obj.get("DeviceIndex"))
        network_card_index = from_int(obj.get("NetworkCardIndex"))
        status = from_str(obj.get("Status"))
        return Attachment(attach_time, attachment_id, delete_on_termination, device_index, network_card_index, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AttachTime"] = self.attach_time.isoformat()
        result["AttachmentId"] = from_str(self.attachment_id)
        result["DeleteOnTermination"] = from_bool(self.delete_on_termination)
        result["DeviceIndex"] = from_int(self.device_index)
        result["NetworkCardIndex"] = from_int(self.network_card_index)
        result["Status"] = from_str(self.status)
        return result


@dataclass
class Group:
    group_id: str
    group_name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Group':
        assert isinstance(obj, dict)
        group_id = from_str(obj.get("GroupId"))
        group_name = from_str(obj.get("GroupName"))
        return Group(group_id, group_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["GroupId"] = from_str(self.group_id)
        result["GroupName"] = from_str(self.group_name)
        return result


@dataclass
class PrivateIPAddress:
    primary: bool
    private_dns_name: str
    private_ip_address: str

    @staticmethod
    def from_dict(obj: Any) -> 'PrivateIPAddress':
        assert isinstance(obj, dict)
        primary = from_bool(obj.get("Primary"))
        private_dns_name = from_str(obj.get("PrivateDnsName"))
        private_ip_address = from_str(obj.get("PrivateIpAddress"))
        return PrivateIPAddress(primary, private_dns_name, private_ip_address)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Primary"] = from_bool(self.primary)
        result["PrivateDnsName"] = from_str(self.private_dns_name)
        result["PrivateIpAddress"] = from_str(self.private_ip_address)
        return result


@dataclass
class NetworkInterface:
    attachment: Attachment
    description: str
    groups: List[Group]
    interface_type: str
    ipv6_addresses: List[Any]
    mac_address: str
    network_interface_id: str
    owner_id: str
    private_dns_name: str
    private_ip_address: str
    private_ip_addresses: List[PrivateIPAddress]
    source_dest_check: bool
    status: str
    subnet_id: str
    vpc_id: str

    @staticmethod
    def from_dict(obj: Any) -> 'NetworkInterface':
        assert isinstance(obj, dict)
        attachment = Attachment.from_dict(obj.get("Attachment"))
        description = from_str(obj.get("Description"))
        groups = from_list(Group.from_dict, obj.get("Groups"))
        interface_type = from_str(obj.get("InterfaceType"))
        ipv6_addresses = from_list(lambda x: x, obj.get("Ipv6Addresses"))
        mac_address = from_str(obj.get("MacAddress"))
        network_interface_id = from_str(obj.get("NetworkInterfaceId"))
        owner_id = from_str(obj.get("OwnerId"))
        private_dns_name = from_str(obj.get("PrivateDnsName"))
        private_ip_address = from_str(obj.get("PrivateIpAddress"))
        private_ip_addresses = from_list(PrivateIPAddress.from_dict, obj.get("PrivateIpAddresses"))
        source_dest_check = from_bool(obj.get("SourceDestCheck"))
        status = from_str(obj.get("Status"))
        subnet_id = from_str(obj.get("SubnetId"))
        vpc_id = from_str(obj.get("VpcId"))
        return NetworkInterface(attachment, description, groups, interface_type, ipv6_addresses, mac_address, network_interface_id, owner_id, private_dns_name, private_ip_address, private_ip_addresses, source_dest_check, status, subnet_id, vpc_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Attachment"] = to_class(Attachment, self.attachment)
        result["Description"] = from_str(self.description)
        result["Groups"] = from_list(lambda x: to_class(Group, x), self.groups)
        result["InterfaceType"] = from_str(self.interface_type)
        result["Ipv6Addresses"] = from_list(lambda x: x, self.ipv6_addresses)
        result["MacAddress"] = from_str(self.mac_address)
        result["NetworkInterfaceId"] = from_str(self.network_interface_id)
        result["OwnerId"] = from_str(self.owner_id)
        result["PrivateDnsName"] = from_str(self.private_dns_name)
        result["PrivateIpAddress"] = from_str(self.private_ip_address)
        result["PrivateIpAddresses"] = from_list(lambda x: to_class(PrivateIPAddress, x), self.private_ip_addresses)
        result["SourceDestCheck"] = from_bool(self.source_dest_check)
        result["Status"] = from_str(self.status)
        result["SubnetId"] = from_str(self.subnet_id)
        result["VpcId"] = from_str(self.vpc_id)
        return result


@dataclass
class Placement:
    availability_zone: str
    group_name: str
    tenancy: str

    @staticmethod
    def from_dict(obj: Any) -> 'Placement':
        assert isinstance(obj, dict)
        availability_zone = from_str(obj.get("AvailabilityZone"))
        group_name = from_str(obj.get("GroupName"))
        tenancy = from_str(obj.get("Tenancy"))
        return Placement(availability_zone, group_name, tenancy)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AvailabilityZone"] = from_str(self.availability_zone)
        result["GroupName"] = from_str(self.group_name)
        result["Tenancy"] = from_str(self.tenancy)
        return result


@dataclass
class PrivateDNSNameOptions:
    enable_resource_name_dns_aaaa_record: bool
    enable_resource_name_dns_a_record: bool
    hostname_type: str

    @staticmethod
    def from_dict(obj: Any) -> 'PrivateDNSNameOptions':
        assert isinstance(obj, dict)
        enable_resource_name_dns_aaaa_record = from_bool(obj.get("EnableResourceNameDnsAAAARecord"))
        enable_resource_name_dns_a_record = from_bool(obj.get("EnableResourceNameDnsARecord"))
        hostname_type = from_str(obj.get("HostnameType"))
        return PrivateDNSNameOptions(enable_resource_name_dns_aaaa_record, enable_resource_name_dns_a_record, hostname_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["EnableResourceNameDnsAAAARecord"] = from_bool(self.enable_resource_name_dns_aaaa_record)
        result["EnableResourceNameDnsARecord"] = from_bool(self.enable_resource_name_dns_a_record)
        result["HostnameType"] = from_str(self.hostname_type)
        return result


@dataclass
class State:
    code: int
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'State':
        assert isinstance(obj, dict)
        code = from_int(obj.get("Code"))
        name = from_str(obj.get("Name"))
        return State(code, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Code"] = from_int(self.code)
        result["Name"] = from_str(self.name)
        return result


@dataclass
class StateReason:
    code: str
    message: str

    @staticmethod
    def from_dict(obj: Any) -> 'StateReason':
        assert isinstance(obj, dict)
        code = from_str(obj.get("Code"))
        message = from_str(obj.get("Message"))
        return StateReason(code, message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Code"] = from_str(self.code)
        result["Message"] = from_str(self.message)
        return result


@dataclass
class Tag:
    key: str
    value: str

    @staticmethod
    def from_dict(obj: Any) -> 'Tag':
        assert isinstance(obj, dict)
        key = from_str(obj.get("Key"))
        value = from_str(obj.get("Value"))
        return Tag(key, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Key"] = from_str(self.key)
        result["Value"] = from_str(self.value)
        return result


@dataclass
class Instance:
    ami_launch_index: int
    architecture: str
    block_device_mappings: List[BlockDeviceMapping]
    capacity_reservation_specification: CapacityReservationSpecification
    client_token: UUID
    cpu_options: CPUOptions
    current_instance_boot_mode: str
    ebs_optimized: bool
    ena_support: bool
    enclave_options: EnclaveOptions
    hibernation_options: HibernationOptions
    hypervisor: str
    image_id: str
    instance_id: str
    instance_type: str
    key_name: str
    launch_time: datetime
    maintenance_options: MaintenanceOptions
    metadata_options: MetadataOptions
    monitoring: Monitoring
    network_interfaces: List[NetworkInterface]
    placement: Placement
    platform_details: str
    private_dns_name: str
    private_dns_name_options: PrivateDNSNameOptions
    private_ip_address: str
    product_codes: List[Any]
    public_dns_name: str
    root_device_name: str
    root_device_type: str
    security_groups: List[Group]
    source_dest_check: bool
    state: State
    state_reason: StateReason
    state_transition_reason: str
    subnet_id: str
    tags: List[Tag]
    usage_operation: str
    usage_operation_update_time: datetime
    virtualization_type: str
    vpc_id: str

    @staticmethod
    def from_dict(obj: Any) -> 'Instance':
        assert isinstance(obj, dict)
        ami_launch_index = from_int(obj.get("AmiLaunchIndex"))
        architecture = from_str(obj.get("Architecture"))
        block_device_mappings = from_list(BlockDeviceMapping.from_dict, obj.get("BlockDeviceMappings"))
        capacity_reservation_specification = CapacityReservationSpecification.from_dict(obj.get("CapacityReservationSpecification"))
        client_token = UUID(obj.get("ClientToken"))
        cpu_options = CPUOptions.from_dict(obj.get("CpuOptions"))
        current_instance_boot_mode = from_str(obj.get("CurrentInstanceBootMode"))
        ebs_optimized = from_bool(obj.get("EbsOptimized"))
        ena_support = from_bool(obj.get("EnaSupport"))
        enclave_options = EnclaveOptions.from_dict(obj.get("EnclaveOptions"))
        hibernation_options = HibernationOptions.from_dict(obj.get("HibernationOptions"))
        hypervisor = from_str(obj.get("Hypervisor"))
        image_id = from_str(obj.get("ImageId"))
        instance_id = from_str(obj.get("InstanceId"))
        instance_type = from_str(obj.get("InstanceType"))
        key_name = from_str(obj.get("KeyName"))
        launch_time = from_datetime(obj.get("LaunchTime"))
        maintenance_options = MaintenanceOptions.from_dict(obj.get("MaintenanceOptions"))
        metadata_options = MetadataOptions.from_dict(obj.get("MetadataOptions"))
        monitoring = Monitoring.from_dict(obj.get("Monitoring"))
        network_interfaces = from_list(NetworkInterface.from_dict, obj.get("NetworkInterfaces"))
        placement = Placement.from_dict(obj.get("Placement"))
        platform_details = from_str(obj.get("PlatformDetails"))
        private_dns_name = from_str(obj.get("PrivateDnsName"))
        private_dns_name_options = PrivateDNSNameOptions.from_dict(obj.get("PrivateDnsNameOptions"))
        private_ip_address = from_str(obj.get("PrivateIpAddress"))
        product_codes = from_list(lambda x: x, obj.get("ProductCodes"))
        public_dns_name = from_str(obj.get("PublicDnsName"))
        root_device_name = from_str(obj.get("RootDeviceName"))
        root_device_type = from_str(obj.get("RootDeviceType"))
        security_groups = from_list(Group.from_dict, obj.get("SecurityGroups"))
        source_dest_check = from_bool(obj.get("SourceDestCheck"))
        state = State.from_dict(obj.get("State"))
        state_reason = StateReason.from_dict(obj.get("StateReason"))
        state_transition_reason = from_str(obj.get("StateTransitionReason"))
        subnet_id = from_str(obj.get("SubnetId"))
        tags = from_list(Tag.from_dict, obj.get("Tags"))
        usage_operation = from_str(obj.get("UsageOperation"))
        usage_operation_update_time = from_datetime(obj.get("UsageOperationUpdateTime"))
        virtualization_type = from_str(obj.get("VirtualizationType"))
        vpc_id = from_str(obj.get("VpcId"))
        return Instance(ami_launch_index, architecture, block_device_mappings, capacity_reservation_specification, client_token, cpu_options, current_instance_boot_mode, ebs_optimized, ena_support, enclave_options, hibernation_options, hypervisor, image_id, instance_id, instance_type, key_name, launch_time, maintenance_options, metadata_options, monitoring, network_interfaces, placement, platform_details, private_dns_name, private_dns_name_options, private_ip_address, product_codes, public_dns_name, root_device_name, root_device_type, security_groups, source_dest_check, state, state_reason, state_transition_reason, subnet_id, tags, usage_operation, usage_operation_update_time, virtualization_type, vpc_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AmiLaunchIndex"] = from_int(self.ami_launch_index)
        result["Architecture"] = from_str(self.architecture)
        result["BlockDeviceMappings"] = from_list(lambda x: to_class(BlockDeviceMapping, x), self.block_device_mappings)
        result["CapacityReservationSpecification"] = to_class(CapacityReservationSpecification, self.capacity_reservation_specification)
        result["ClientToken"] = str(self.client_token)
        result["CpuOptions"] = to_class(CPUOptions, self.cpu_options)
        result["CurrentInstanceBootMode"] = from_str(self.current_instance_boot_mode)
        result["EbsOptimized"] = from_bool(self.ebs_optimized)
        result["EnaSupport"] = from_bool(self.ena_support)
        result["EnclaveOptions"] = to_class(EnclaveOptions, self.enclave_options)
        result["HibernationOptions"] = to_class(HibernationOptions, self.hibernation_options)
        result["Hypervisor"] = from_str(self.hypervisor)
        result["ImageId"] = from_str(self.image_id)
        result["InstanceId"] = from_str(self.instance_id)
        result["InstanceType"] = from_str(self.instance_type)
        result["KeyName"] = from_str(self.key_name)
        result["LaunchTime"] = self.launch_time.isoformat()
        result["MaintenanceOptions"] = to_class(MaintenanceOptions, self.maintenance_options)
        result["MetadataOptions"] = to_class(MetadataOptions, self.metadata_options)
        result["Monitoring"] = to_class(Monitoring, self.monitoring)
        result["NetworkInterfaces"] = from_list(lambda x: to_class(NetworkInterface, x), self.network_interfaces)
        result["Placement"] = to_class(Placement, self.placement)
        result["PlatformDetails"] = from_str(self.platform_details)
        result["PrivateDnsName"] = from_str(self.private_dns_name)
        result["PrivateDnsNameOptions"] = to_class(PrivateDNSNameOptions, self.private_dns_name_options)
        result["PrivateIpAddress"] = from_str(self.private_ip_address)
        result["ProductCodes"] = from_list(lambda x: x, self.product_codes)
        result["PublicDnsName"] = from_str(self.public_dns_name)
        result["RootDeviceName"] = from_str(self.root_device_name)
        result["RootDeviceType"] = from_str(self.root_device_type)
        result["SecurityGroups"] = from_list(lambda x: to_class(Group, x), self.security_groups)
        result["SourceDestCheck"] = from_bool(self.source_dest_check)
        result["State"] = to_class(State, self.state)
        result["StateReason"] = to_class(StateReason, self.state_reason)
        result["StateTransitionReason"] = from_str(self.state_transition_reason)
        result["SubnetId"] = from_str(self.subnet_id)
        result["Tags"] = from_list(lambda x: to_class(Tag, x), self.tags)
        result["UsageOperation"] = from_str(self.usage_operation)
        result["UsageOperationUpdateTime"] = self.usage_operation_update_time.isoformat()
        result["VirtualizationType"] = from_str(self.virtualization_type)
        result["VpcId"] = from_str(self.vpc_id)
        return result


@dataclass
class Reservation:
    groups: List[Any]
    instances: List[Instance]
    owner_id: str
    reservation_id: str

    @staticmethod
    def from_dict(obj: Any) -> 'Reservation':
        assert isinstance(obj, dict)
        groups = from_list(lambda x: x, obj.get("Groups"))
        instances = from_list(Instance.from_dict, obj.get("Instances"))
        owner_id = from_str(obj.get("OwnerId"))
        reservation_id = from_str(obj.get("ReservationId"))
        return Reservation(groups, instances, owner_id, reservation_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Groups"] = from_list(lambda x: x, self.groups)
        result["Instances"] = from_list(lambda x: to_class(Instance, x), self.instances)
        result["OwnerId"] = from_str(self.owner_id)
        result["ReservationId"] = from_str(self.reservation_id)
        return result


@dataclass
class HTTPHeaders:
    cache_control: str
    content_length: int
    content_type: str
    date: str
    server: str
    strict_transport_security: str
    vary: str
    x_amzn_requestid: UUID

    @staticmethod
    def from_dict(obj: Any) -> 'HTTPHeaders':
        assert isinstance(obj, dict)
        cache_control = from_str(obj.get("cache-control"))
        content_length = int(from_str(obj.get("content-length")))
        content_type = from_str(obj.get("content-type"))
        date = from_str(obj.get("date"))
        server = from_str(obj.get("server"))
        strict_transport_security = from_str(obj.get("strict-transport-security"))
        vary = from_str(obj.get("vary"))
        x_amzn_requestid = UUID(obj.get("x-amzn-requestid"))
        return HTTPHeaders(cache_control, content_length, content_type, date, server, strict_transport_security, vary, x_amzn_requestid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["cache-control"] = from_str(self.cache_control)
        result["content-length"] = from_str(str(self.content_length))
        result["content-type"] = from_str(self.content_type)
        result["date"] = from_str(self.date)
        result["server"] = from_str(self.server)
        result["strict-transport-security"] = from_str(self.strict_transport_security)
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
class DescribeInstanceResponseDTO:
    reservations: List[Reservation]
    response_metadata: ResponseMetadata

    @staticmethod
    def from_dict(obj: Any) -> 'DescribeInstanceResponseDTO':
        assert isinstance(obj, dict)
        reservations = from_list(Reservation.from_dict, obj.get("Reservations"))
        response_metadata = ResponseMetadata.from_dict(obj.get("ResponseMetadata"))
        return DescribeInstanceResponseDTO(reservations, response_metadata)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Reservations"] = from_list(lambda x: to_class(Reservation, x), self.reservations)
        result["ResponseMetadata"] = to_class(ResponseMetadata, self.response_metadata)
        return result


def describe_instance_response_dto_from_dict(s: Any) -> DescribeInstanceResponseDTO:
    return DescribeInstanceResponseDTO.from_dict(s)


def describe_instance_response_dto_to_dict(x: DescribeInstanceResponseDTO) -> Any:
    return to_class(DescribeInstanceResponseDTO, x)


class DescribeInstanceResponseParser:
    ''' Main class to call the serializer'''
    def describeInstanceResponseParsed(self,response_json):
        '''

        :param response_json: Json value of the Describe Instance response
        :return: Serialized Json class of the response
        '''
        return describe_instance_response_dto_from_dict(response_json)