Change Log
~~~~~~~~~~
All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/>`_.

====================
2.155.2 - 2025-07-15
====================

Added 
----- 
* Support for calling Oracle Cloud Infrastructure services in the ap-delhi-1 region
2.155.1 - 2025-07-08
====================

Added 
----- 
* Support for calling Oracle Cloud Infrastructure services in the us-ashburn-2 region 
* Support for insight of Autonomous Database on Exadata Cloud@Customer (ADB on ExaC@C) in the Operations Insights service 
* Support for Spanish and Portuguese language recognition with Azure-backed Optical Character Recognition (OCR) in the AI Document service 
* Support for UK, Australian, and Canadian address and tax form recognition in the AI Document service 
* Support for Personal-to-Corporate conversation check in the OSP Gateway service   

====================
2.155.0 - 2025-07-01
====================

Added 
----- 
* Support for the Database MultiCloud service 
* Support for System Tags in the Database service 
* Support for PKCS11 Library Integration for Azure Key Store in the Database service 
* Support for changing subscription ID and the opc-dry-run parameter in the Database service 
* Support for listing all members of an Elastic Resource Pool for a provided Elastic Resource Pool leader in the Database service 
* Support for managing scheduled queries in the Application Performance Monitoring service 
* Support for Bring Your Own Key (BYOK) in the MySQL Heatwave service 
* Support for customer-initiated collection of diagnostic information in the Database Migration service   

Breaking 
-------- 
* The type of field `state` has been changed from string to `state` enum in the models `AutoActivateToggleStatus` and `AutoActivateStatus` in the Application Performance Monitoring service   

====================
2.154.3 - 2025-06-24
====================

Added 
----- 
* Support for database backups to Amazon S3 as default option for all databases running on Exa@AWS in the Database service 
* Support for customer-managed encryption keys in hosted environments in the NoSQL Database service 
* Support for upgrading a fleet of Grid Infrastructure and Databases to 23ai for ExaCS and ExaCC in the Exadata Fleet Update service 
* Support for Bring Your Own IPv6 (BYOIPv6) in the Load Balancer service   

====================
2.154.2 - 2025-06-17
====================

Added 
----- 
* Support for node cycling (reboot/replaceBootVolume) for worker nodes in the Kubernetes Engine service 
* Support for the WebLogic Management service 
* Support for the Privileged API Access Control service 
* Support for Role Based Access Control List in the OCI Cache service 
* Support for integrating native Redis authentication with OCI Identity/IAM in the OCI Cache service 
* Support for Command String in Runcommand API in the Instance Agent service 
* Support for new fields capacitySummary and computeBareMetalHostId in the API response when fetching Dedicated Virtual Machine Hosts in the Compute service   

====================
2.154.1 - 2025-06-10
====================

Added 
----- 
* Support for performing an explicit Data Guard pre-check by setting new optional dry-run parameter when creating a database in the Database service   

====================
2.154.0 - 2025-06-03
====================

Added 
----- 
* Support for creating auto Autonomous Container Database backups in a remote region in the Database service 
* Support for creating new Autonomous Container Databases from a backup in the remote region in the Database service 
* Support for input/output token usage information in the Generative AI Agent service 
* Support for standby connection in the Database Management service 
* Support for additional metrics, including replication metrics, in the Database Management service 
* Support for replication dashboard in the Database Management service 
* Support for soft-deleting backups in the HeatWave service 
* Support for additional connections types for Oracle Rest Data Services (ORDS), Apache Iceberg, and IBM Db2 for i in the Golden Gate service   

Breaking 
-------- 
* Constants `SERVICE_LEVEL_AGREEMENT_TYPE_STANDARD`, `SERVICE_LEVEL_AGREEMENT_TYPE_AUTONOMOUS_DATAGUARD`, `PROTECTION_MODE_MAXIMUM_AVAILABILITY`, `PROTECTION_MODE_MAXIMUM_PERFORMANCE`, `PATCH_MODEL_RELEASE_UPDATES`, `PATCH_MODEL_RELEASE_UPDATE_REVISIONS`, `VERSION_PREFERENCE_NEXT_RELEASE_UPDATE`, `VERSION_PREFERENCE_LATEST_RELEASE_UPDATE`, `DISTRIBUTION_AFFINITY_MINIMUM_DISTRIBUTION`, `DISTRIBUTION_AFFINITY_MAXIMUM_DISTRIBUTION`, `NET_SERVICES_ARCHITECTURE_DEDICATED`, `NET_SERVICES_ARCHITECTURE_SHARED` moved from model `CreateAutonomousContainerDatabaseDetails` to `CreateAutonomousContainerDatabaseBase` in the Database service 
* Properties `customer_contacts`, `display_name`, `db_unique_name`, `db_name`, `service_level_agreement_type`, `autonomous_exadata_infrastructure_id`, `db_version`, `database_software_image_id`, `peer_autonomous_exadata_infrastructure_id`, `peer_autonomous_container_database_display_name`, `protection_mode`, `fast_start_fail_over_lag_limit_in_seconds`, `is_automatic_failover_enabled`, `peer_cloud_autonomous_vm_cluster_id`, `peer_autonomous_vm_cluster_id`, `peer_autonomous_container_database_compartment_id`, `peer_autonomous_container_database_backup_config`, `peer_db_unique_name`, `autonomous_vm_cluster_id`, `cloud_autonomous_vm_cluster_id`, `compartment_id`, `patch_model`, `maintenance_window_details`, `standby_maintenance_buffer_in_days`, `version_preference`, `is_dst_file_update_enabled`, `freeform_tags`, `defined_tags`, `backup_config`, `kms_key_id`, `kms_key_version_id`, `vault_id`, `key_store_id`, `db_split_threshold`, `vm_failover_reservation`, `distribution_affinity`, `net_services_architecture` moved from model `CreateAutonomousContainerDatabaseDetails` to `CreateAutonomousContainerDatabaseBase` in the Database service 
* Property `user_id` changed from required to optional for model `OracleNosqlConnectionSummary` in the Golden Gate service   

====================
2.153.0 - 2025-05-27
====================

Added 
----- 
* Support for List and Get APIs for out-of-box management dashboard resources in the Management Dashboard service 
* Support for REST option in the HeatWave MySQL service 
* Support for warnings in list-application-dependency-vulnerability response for vulnerability audits in the Adm service 
* Support for HostGroups in the Compute service 
* Support for ENTERPRISE_EDITION_DEVELOPER enum in Db System Launch and Create DB external backup commands in the Database service 
* Support for databaseEditionQueryParam in dbSystemInitialStorageSizes, dbSystemStoragePerformance, quotaDefinitions, and internalQuotaDefinitions in the Database service 
* Support for EmissionType parameter in UsageCarbonEmissionSummary and EmissionCalculationMethod, EmissionType, Granularity parameters in UsageCarbonEmissionsReportQuery in the Usage Api service 
* Support for querying capacity report under BDSs tenancy in the Big Data service 
* Support for installing Dataplane Software and python packages updates in the Big Data service 
* Support for triggering a dry run with OS patch in the Big Data service 
* Support for NAT on firewall feature in the Network Firewall service 
* Support for Predictable OIDC Discovery in the OKE service 
* Support for SQL and FTP monitoring, creating and updating in the Application Performance Monitoring Synthetic service 
* Support for Demand signal feature in the Capacity Management service 
* Support for Targeted Launch in the Launch Instance API service   

Breaking 
-------- 
* Constants `LIFECYCLE_STATE_ATTACHING` and `LIFECYCLE_STATE_DETACHING` are removed from models `NetworkFirewallPolicySummary`, `NetworkFirewallPolicy`, `NetworkFirewallSummary` and `NetworkFirewall` in the Network Firewall service   

====================
2.152.1 - 2025-05-20
====================

Added 
----- 
* Support for the Globally Distributed Database service 
* Support for listing the available upgrades (OS & GI) for VirtualMachine DB systems in the Database service 
* Support for running dry-run operations in the Database service 
* Support for Network Security Groups in MySQL HeatWave service

====================
2.152.0 - 2025-05-13
====================

Added 
----- 
* Support for the Model Deployment service  
* Support for enabling and monitoring Pluggable Databases(PDB) in the Database Management service 
* Support for additional unit shapes in AI clusters in the Generative AI service 
* Support for node search details and node shape details on create and update cluster operations in the OpenSearch service   

Breaking 
-------- 
* Models `DisableExternalMysqlAssociatedServiceDetails` and `EnableExternalMysqlAssociatedServiceDetails` removed from the Database Management service 
* Property `lifecycle_state` removed from model `ExadataInfrastructureLifecycleStateValues` in the Database Management service 
* Operations `disable_external_mysql_associated_service` and `enable_external_mysql_associated_service` removed from `ManagedMySqlDatabasesClient` in the Database Management service 
* Default retries disabled for operations `get_named_credential` and `list_named_credentials` from `DbManagementClient` in the Database Management service 
* Operation `modify_external_container_database_management_feature` removed from `DbManagementClient` in the Database Management service   

====================
2.151.0 - 2025-05-06
====================

Added 
----- 
* Support for dry run while creating cloud exadata Infrastructure and VM clusters in the Database service 
* Support for filters to get latest versions on list system versions API in the Database service 
* Support for generic fleets without fleet type in the Fleet Application Management service 
* Support for creating resources and changing compartment in the Fleet Application Management service 
* Support for infrastructure management via provisioning with terraform based catalog items and deployments in the Fleet Application Management service 
* Support for platform configuration metadata management in the Fleet Application Management service 
* Support for managing runbook versions in the Fleet Application Management service 
* Support for provisioning runbooks in the Fleet Application Management service 
* Support for resource inventory in the Fleet Application Management service 
* Support for changing compartment for fleets, platforms configurations, properties, patches, runbooks and task resources in the Fleet Application Management service 
* Support for new migration phase in the Database migration service   

Breaking 
-------- 
* Models `Associations` and `NotificationPreferences` were removed from the Fleet Application Management service 
* Properties `resource_id` ,`name`, `type`, `application_type`, `runbook_id` are removed from model `ActionGroupDetails` in the Fleet Application Management service 
* Properties `resource_id`, `type`, `application_type`, `product`, `lifecycle_operation`, `runbook_id`, `target_id`, `subjects` are removed from model `ActionGroup` in the Fleet Application Management service 
* Property `tenancy_id` is removed from model `AssociatedSchedulerDefinition` in the Fleet Application Management service 
* Property `patch_type` is removed from models `CompliancePolicyRuleSummary` and `CompliancePolicyRule` in the Fleet Application Management service 
* Property `condition` is removed from model `ComponentProperties` in the Fleet Application Management service 
* Properties `patch_type` and `compartment_id` are removed from model `CreateCompliancePolicyRuleDetails` in the Fleet Application Management service 
* Property `compartment_id` is removed from models `CreateFleetCredentialDetails` `CreateFleetPropertyDetails`, `UpdatePatchDetails` in the Fleet Application Management service 
* Properties `fleet_type` ,`application_type`, `group_type`, `resource_selection_type`, `rule_selection_criteria` are removed from model `CreateFleetDetails` in the Fleet Application Management service 
* Properties `maintenance_window_type` and `task_initiation_cutoff` are removed from models `CreateMaintenanceWindowDetails`, `MaintenanceWindowSummary`, `MaintenanceWindow`, `UpdateMaintenanceWindowDetails` in the Fleet Application Management service 
* Properties `runbook_relevance` and `associations` are removed from models `CreateRunbookDetails` and `Runbook` in the Fleet Application Management service 
* Property `activity_initiation_cut_off` is removed from model `CreateSchedulerDefinitionDetails` in the Fleet Application Management service 
* Property `application_type` is removed from models `FleetResource` and `FleetResourceSummary` in the Fleet Application Management service 
* Property `fleet_type` is removed from model `FleetSummary` in the Fleet Application Management service 
* Properties `application_type`, `group_type`, `resource_selection_type`, `rule_selection_criteria` are removed from model `Fleet` in the Fleet Application Management service 
* Property `id` is removed from model `OperationRunbook` in the Fleet Application Management service 
* Property `on_upcoming_schedule` is removed from model `Preferences` in the Fleet Application Management service 
* Property `runbook_relevance` is removed from model `RunbookSummary` in the Fleet Application Management service 
* Properties `maintenance_window_id`, `recurrences`, `duration` are removed from model `Schedule` in the Fleet Application Management service 
* Properties `tenancy_id`, `action_group_types`, `application_types` are removed from model `ScheduledFleetSummary` in the Fleet Application Management service 
* Properties `action_group_types`, `application_types` are removed from models `ScheduledFleetSummary`, `SchedulerDefinitionSummary`, `SchedulerDefinition` in the Fleet Application Management service 
* Properties `action_group_types`, `application_types`, `associated_schedule_definition` are removed from models `SchedulerJob`, `SchedulerJobSummary` in the Fleet Application Management service 
* Property `value` is removed from model `TaskArgument` in the Fleet Application Management service 
* Property `association_type` is removed from model `Task` in the Fleet Application Management service 
* Property `patch_type` is removed from model `UpdateCompliancePolicyRuleDetails` in the Fleet Application Management service 
* Property `rule_selection_criteria` is removed from model `UpdateFleetDetails` in the Fleet Application Management service 
* Properties `associations`, `runbook_relevance` are removed from model `UpdateRunbookDetails` in the Fleet Application Management service 
* Property `activity_initiation_cut_off` is removed from model `UpdateSchedulerDefinitionDetails` in the Fleet Application Management service 
* Property `display_name` changed from optional to required in models `CreatePlatformConfigurationDetails`, `CreateTaskRecordDetails` and `CreatePropertyDetails` in the Fleet Application Management service 
* Type of property `content` changed to `PatchFileContentDetails` from `ContentDetails` in models `GenericArtifact` and `PlatformSpecificArtifact` in the Fleet Application Management service 
* Return type for property `notification_preferences` changed to `list[NotificationPreference]` from `NotificationPreferences` in model `UpdateFleetDetails` in the Fleet Application Management service 
* Operations `get_work_request` , `list_work_request_errors` , `list_work_requests` , `list_work_request_logs` are removed from `FleetAppsManagementClient` in the Fleet Application Management service 
* Parameter `compartment_id` is removed from operation `list_fleet_properties` in the `FleetAppsManagementClient` in the Fleet Application Management service 
* Parameter `tenancy_id` is removed from operation `list_fleet_resources` in the `FleetAppsManagementClient` in the Fleet Application Management service 
* Parameter `compartment_id` is removed from operation `list_scheduled_fleets` in the `FleetAppsManagementOperationsClient` in the Fleet Application Management service 
* Parameters `sub_state` and `defintion_id` are removed from operation `list_scheduler_jobs` in the `FleetAppsManagementOperationsClient` in the Fleet Application Management service 
* Parameter `runbook_relevance` is removed from operation `list_runbooks` in the `FleetAppsManagementRunbooksClient` in the Fleet Application Management service   

====================
2.150.3 - 2025-04-29
====================

Added 
----- 
* Support for custom headers for model retirement in the Generative AI service 
* Support for usage statistics in the responses of Cohere chat and embed APIs in the Generative AI service 
* Support for custom pre-checks in disaster recovery plans in the Disaster Recovery service 
* Support for retention of automatic backups in the database system deletion policy in the HeatWave service 
* Support for updating compartment of schedules in the Resource Scheduler service 
* Support for listing schedules by resource identifier in the Resource Scheduler service 
* Support for custom parameters when creating schedules in the Resource Scheduler service  

====================
2.150.2 - 2025-04-21
====================

Added 
----- 
* Support for patch management in the Database Lifecycle Management service 
* Support for restricting public network access to service instances in the Visual Builder service 
* Support for iSCSI-3 persistent reservations on block volume in the Core services (Networking, Compute, Block Volume)   

Fixed 
----- 
* Limited the `enable_fips` method in `oci.fips` module to work only on OpenSSL 1.x for compatibility with OpenSSL 3.x   

====================
2.150.1 - 2025-04-15
====================

Added
-----
* Support for applying guardrails, enabling content moderation and detection of Prompt Injection and Personally Identifiable Information (PII) in the Generative AI Inference service
* Support for providing customer contacts for operational notifications in the Database service

2.150.0 - 2025-04-08
====================

Added 
----- 
* Support for connector source and targets with private endpoints in the Resource Scheduler service 
* Support for Cross Region Replication(XRR) for external key managers in the Key Management service 
* Support for dry run of function invocation in the Functions service 
* Support for collecting diagnostics for ZeroETL pipelines in the GoldenGate service 
* Support for adding, removing and switchover to local peers of deployment in different availability and fault domains within in the same region in the GoldenGate service 
* Support for creating standby deployments in the GoldenGate service   

Breaking 
-------- 
* The property `kind` in the `SourceDetails`, `TaskDetails` and `TargetDetails` models in the Resource Scheduler service was fixed to no longer support `UNKNOWN_ENUM_VALUE`. Instead, a `ValueError` will be raised if this property is assigned a value that it does not support. 
* The type of property `source` in model `ServiceConnector` changed from `oci.sch.models.SourceDetails` to `oci.sch.models.SourceDetailsResponse` in the Resource Scheduler service 
* The type of property `tasks` in model `ServiceConnector` changed from `oci.sch.models.TargetDetails` to `oci.sch.models.TaskDetailsResponse` in the Resource Scheduler service 
* The type of property `target` in model `ServiceConnector` changed from `oci.sch.models.TaskDetails` to `oci.sch.models.TargetDetailsResponse` in the Resource Scheduler service   

====================
2.149.2 - 2025-04-01
====================

Added 
----- 
* Support for the Lustre File service 
* Support for machine learning applications in the Data Science service 
* Support for action endpoints to export and import configurations in the Application Performance Monitoring service 
* Support for ECPU (Elastic Compute Unit) compute model based warehouses in the Operations insights service   

====================
2.149.1 - 2025-03-25
====================

Added 
----- 
* Support for agent platforms and Retrieval Augmented Generation (RAG) agents in the Generative AI Agent service 
* Support for knowledge based metadata summaries in the Generative AI Agent service 
* Support for create and update operations on onboard configurations in the Stack Monitoring service 
* Support for automatic activation of the management agents on compute instance launch in the Stack Monitoring service 
* Support for importing collectd resources in the Stack Monitoring service 
* Support for updating the handler configurations for collected resources in Stack Monitoring service 
* Support for monitored resource types based on source type and resource category in the Stack Monitoring service 
* Support for adding tags in maintenance windows in the Stack Monitoring service 
* Support for host API feature in the Compute service   

====================
2.149.0 - 2025-03-18
====================

Added 
----- 
* Support for Managed Services for Mac service 
* Support for scheduling customer-initiated backups in the GoldenGate service 
* Support for GPU memory clusters and fabrics in the Compute service   

Breaking 
-------- 
* The properties `ip_anycast_id` and `monitor_ip` were removed from the models `CreateByoipRangeDetails` and `UpdateByoipRangeDetails` in the Compute service   

====================
2.148.0 - 2025-03-11
====================

Added 
----- 
* Support for pipelines in the OpenSearch service 
* Support for uploading and downloading the model metadata artifacts in the Data Science service 
* Support for model references via native API in the Data Science service 
* Support for scheduling cross-region database backups in the HeatWave service 
* Support for specifying backup retention days for manual cross-region backups in the HeatWave service 
* Support for IPv6 addresses for dedicated infrastructure in the Database service 
* Support for NewDev edition for the development community in the Database service 
* Support for grouping sensitive types across the tenancies and reuse of groups in the discovery workflow in the Data Safe service 
* Support for generating custom assessment reports in the Data Safe service   

Breaking 
-------- 
* The properties `max_memory_gb`, `max_ocpu_count`, `min_memory_gb`, `min_ocpu_count` were removed from the models `CreateOpensearchClusterPipelineDetails`, `OpensearchClusterPipeline`, `OpensearchClusterPipelineSummary`, and `UpdateOpensearchClusterPipelineDetails` in the OpenSearch service 
* The property `system_tags` was removed from the model `CreateOpensearchClusterPipelineDetails` in the OpenSearch service 
* The models `OpensearchPipelineValidationResponse`, `ValidateOpensearchPipelineDetails`, and `PipelineValidationErrorDetails` were removed in the OpenSearch service   

====================
2.147.0 - 2025-03-04
====================

Added 
----- 
* Support for user quotas on file system resources in the File Storage service 
* Support for long term retention backups in the Autonomous Recovery service 
* Support for Cross Region Replication(CRR) in the PostgreSQL service 
* Support for subscriptions and cluster placement groups on exascale infrastructure in the Database service 
* Support for multiple standby databases for autonomous dataguard associations in the Database service 
* Support for major version upgrade of clusters in the OpenSearch service 
* Support for Customer Service Identifier(CSI) number in list assigned subscriptions response in the Organizations service   

Breaking 
-------- 
* Operation `create_subscription_mapping_and_wait_for_state` waits on `SubscriptionMapping.lifecycle_state` instead of `WorkRequest` in the Organizations service   

====================
2.146.0 - 2025-02-25
====================

Added 
----- 
* Support for Database Lifecycle Management service 
* Support for Valkey cluster creation and Valkey migration in the OCI Cache service 
* Support for Dataflow Steps and Storage Mounts in Pipelines in the Data Science service 
* Support for Bring Your Own DKIM Keys in the Email Delivery service 
* Support for OpenId Connect Multi Authentication command in the OCI Kubernetes Engine service 
* Support for security attributes for Load Balancer resource in the Load Balancer service 
* Support for reservation of private IP addresses in the Networking service 
* Support for additional configuration parameters in the HeatWave service 
* Support for private and 3rd party software repositories, and rebooting of instances in the OS Management service 

Breaking 
-------- 
* The property `zpr_tags` was removed from models `UpdateLoadBalancerDetails`, `CreateLoadBalancerDetails` and `LoadBalancer` in the Load Balancer service 
* The models `CreateContainerCommandHealthCheckDetails` and `ContainerCommandHealthCheck` were removed in the Container Instances service 
* The allowed value `COMMAND` was removed from the property `health_check_type` in the models `ContainerHealthCheckType`, `ContainerHttpHealthCheck` and `ContainerTcpHealthCheck` in the Container Instances service 

====================
2.145.0 - 2025-02-18
====================

Added 
----- 
* Support for Customer Onboarding Success(COS) in the Java Management service 
* Support for filtering performance tuning analysis results in the Java Management service 
* Support for improved plugin filtering in the Java Management service 
* Support for operating system distribution information in the Java Management service   

Fixed 
----- 
* 

Fixed an issue in RPv2.1 to read private key from a file   

Breaking 
-------- 
* put_object failures for 412 status code have been fixed. This might be a breaking change for customers who have defined a custom exception handler for 412 status code (#622)    

====================
2.144.1 - 2025-02-11
====================

Added 
----- 
* Support for backups and recovery enhancements in autonomous databases in the Database service 
* Support for IPv6 addresses on system launch in the Database service 
* Support for enterprise edition GPU infrastructure in the Stack Monitoring service 
* Support for monitoring templates in the Stack Monitoring service 
* Support for IPv6 cluster creation in the Kubernetes Engine service 
* Support for automatic and spoken punctuations in realtime in the AI Speech service 
* Support for additional connection types for Databricks, Google PubSub and Microsoft Fabric in the GoldenGate service   

====================
2.144.0 - 2025-02-04
====================

Added 
----- 
* Support for Cohere Embed v3 in the Generative AI Inference service 
* Support for Llama 3.2 tools in the Generative AI Inference service 
* Support for nginx discovery and monitoring in the Stack Monitoring service 
* Support for Oracle JVM runtime discovery and monitoring in the Stack Monitoring service 
* Support for JBoss discovery and monitoring in the Stack Monitoring service 
* Support for Service Managed Container(SMC) endpoints on list service operation in the Data Science service 
* Support for schedulers in the Data Science service 
* Support for DB system database and access modes in the HeatWave service 
* Support for DB system read endpoints in the HeatWave service 
* Support for sensitive types for data discovery in the Data Safe service 
* Support for referential relation APIs in the Data Safe service   

Breaking 
-------- 
* The models `CreateAuditPolicyDetails` and `CreateAuditProfileDetails` were removed in the Data Safe service   

====================
2.143.1 - 2025-01-28
====================

Added 
----- 
* Support for external MySQL database management in the Database Management service 
* Support for fetching highly available metrics for managed databases in the Database Management service 
* Support for Exadata Infrastructure on Exadata Cloud@Customer in the Database service 
* Support for disaster recovery for cloud native applications running on OKE clusters in the Disaster Recovery service 
* Support for subscription assignment at creation of the child tenancies in the Organizations service 
* Support for additional actionable insights content-types for news reports in the Operations Insights service 
* Support for MySQL Heatwave database systems in the Operations Insights service   

====================
2.143.0 - 2025-01-21
====================

Added 
----- 
* Support for Bring Your Own ASN (BYOASN) in the Networking service 
* Support for Data Guard transaction processing in the Database service 
* Support for permanently disconnecting peer autonomous databases from its primary database in the Database service 
* Support for databases with external Hardware 

Security Module (HSM) in the Database service 
* Support for active and standby purist modes in the Network Load Balancer service 
* Support for configurable TCP reset in the Network Load Balancer service   

Breaking 
--------
* Fixed 413 error for put operation of very large object in object storage service

====================
2.142.0 - 2025-01-14
====================

Added
-----
* Support for attaching route tables to VNICs and private IPs in the Networking service
* Support for Cross Cluster Search(CCS) for an opensearch cluster in the OpenSearch service
* Support for patch-level updates of the autonomous databases after provisioning in the Database service

Breaking
--------
* put_object failures for 412 status code have been fixed. This might be a breaking change for customers who have defined a custom exception handler for 412 status code (https://github.com/oracle/oci-python-sdk/issues/622)

====================
2.141.1 - 2024-12-20
====================

Fixed
-----
* `Github Issue #728 <https://github.com/oracle/oci-python-sdk/issues/728>`_ for RPv1.1

====================
2.141.0 - 2024-12-17
====================

Added 
----- 
* Support for backup retention locks on autonomous database create and update operations in the Database service 
* Support for multi-modality flags in data source in the Generative AI service 
* Support for knowledge base statistics in the Generative AI service 
* Support for document id, title and page numbers in citations in the Generative AI service 
* Support for creating and updating Amazon Web Services (AWS) asset-sources, EC2 and Elastic Block Store (EBS) assets in the Cloud Bridge service 
* Support for listing Amazon Web Services (AWS) regions available for discovery and migrations in the Cloud Bridge service 
* Support for stored video analysis in the AI Vision service 
* Support for HTTP or REST endpoint-based metric extensions in the OCI Monitoring service 
* Support for metric extension filter in the list metric extensions operation in the OCI Monitoring service 
* Support for creating and updating private endpoints for model deployments in the Data Science service 
* Support for OCI Identity user integration in the Big Data service 
* Support for user principal session tokens in the Big Data service 
* Support for historical cluster versions in the Big Data service 
* Support for new SKUs for digital assets editions in the Blockchain Platform service 
* Support for Zero ETL pipelines in the GoldenGate service   

Breaking 
-------- 
* Removed fallback to the deprecated Instance Metadata service (IMDS) V1 endpoint 
* `INSTANCE_METADATA_URL_CERTIFICATE_RETRIEVER_RETRY_STRATEGY` was modified to do 8 retry attempts and exponential backoff with Jitter between attempts, instead of 3 fixed interval retries  
* Parameter `compartment_id` in operation `list_metric_extensions` was removed from the `StackMonitoringClient` in the OCI Monitoring service   

====================
2.140.0 - 2024-12-10
====================

Added 
----- 
* Support for Bring Your Own Key (BYOK) in the Database service 
* Support for refreshing disaster recovery plans in the Disaster Recovery service 
* Support for private access to service instances in the Visual Builder service 
* Support for exadata fleet update and rollback maintenance cycle in the Fleet Application Management service 
* Support for Bring Your Own License (BYOL) for windows virtual machines in the Compute service 
* Support for cascading deletion of applications and runs in the Data Flow service 
* Support for on-demand translation and auto language detection during file translation in the AI Language service 
* Support for alias for endpoints in custom model flow and custom anonymization in the AI Language service   

Breaking 
-------- 
* Models `IdcsInfoDetails` and `AttachmentDetails` were removed from the Visual Builder service 
* Parameters `idcs_info` and `attachments` were removed from the model `VbInstance` in the Visual Builder service   

====================
2.139.0 - 2024-11-19
====================

Added 
----- 
* Support for optional parameters for unified auditing in the Database service 
* Support for user groups for creating technical requests in the Support Management service 
* Support for additional checksum algorithms (SHA-256, SHA-384, CRC32C) in the Object Storage service 
* Support for single Read Only (RO) endpoint for the read replicas in the PostgreSQL service 
* Support for exascale database vaults in the Database service 
* Support for virtual machine clusters with database vaults in the Database service 
* Support for N3-Gi version in the Database service   

Changed 
------- 
* The vendored library idna was upgraded from version `2.10` to `3.10` 
* The vendored library urllib3 was upgraded from version `1.26.9` to `1.26.20`   

Breaking 
-------- 
* The property `sub_components` was removed from the model `SubCategories` in the Customer Incident Management Service 
* The constants `LIMIT_STATUS_APPROVED`, `LIMIT_STATUS_PARTIALLY_APPROVED`, `LIMIT_STATUS_NOT_APPROVED`, `LIMIT_STATUS_REJECTED` were removed from the model `CreateLimitItemDetails` in the Customer Incident Management Service 
* The property `limit_status` was removed from the model `CreateLimitItemDetails` in the Customer Incident Management Service 
* The model `ServiceCategories` was removed from the Customer Incident Management Service   

====================
2.138.1 - 2024-11-12
====================

Added 
----- 
* Support for calling Oracle Cloud Infrastructure services in the me-alain-1 region 
* Support for connection refresh in the GoldenGate service 
* Support for secret compartment id in import and export operations of deployment wallet in the GoldenGate service 
* Support for creating metadata only backups in the GoldenGate service 
* Support for Llama 3.2 unit shape in Generative AI service 
* Support for Llama 3.2 vision in Generative AI Inference service 
* Support for Cohere CommandR response format in Generative AI Inference service   

====================
2.138.0 - 2024-11-05
====================

Added 
----- 
* Support for calling Oracle Cloud Infrastructure services in the ap-seoul-2 region 
* Support for calling Oracle Cloud Infrastructure services in the ap-suwon-1 region 
* Support for calling Oracle Cloud Infrastructure services in the ap-chuncheon-2 region 
* Support for MFA Enablement v2 in the Identity Domains service 
* Support for starting, stopping and updating min/max executor count for SQL Endpoints in the Data Flow service 
* Support for customer message in the Customer Incident Management Service 
* Support for REJECTED limitStatus in the Customer Incident Management Service   

Fixed 
----- 
* Issue with using `OkeWorkloaIdentityResourcePrincipalSigner` after the PyJWT upgrade to 2.4.0 introduced int OCI Python SDK `2.137.1` 
* UserWarning being emitted from Cryptography 43.x   

Breaking 
-------- 
* The operations `get_status` and `get_csi_number` were removed from the IncidentClient in the Customer Incident Management Service 
* The property `service_categories` was removed from the model `IncidentResourceType` in the Customer Incident Management Service 
* The properties `service_category` and `issue_type` were removed from the model `ServiceCategories` in the Customer Incident Management Service 
* The retry strategy for getting the X509 token from Identity service was modified and is now protected via circuit breaker   

====================
2.137.1 - 2024-10-29
====================

Added 
----- 
* Support for L3IP (Layer 3 IP) listeners in the Network Load Balancing service 
* Support for overriding an existing add-on installation in the Kubernetes Engine service   

====================
2.137.0 - 2024-10-22
====================

Added 
----- 
* Support for resource locking in the File storage service 
* Support for customer managed keys via Azure key vault and Amazon Web Services key vault in the Database service 
* Support for generated tokens on create secret operations in the Identity Domains service 
* Support for creating and updating Amazon Web Services asset-sources, EC2 and EBS assets in the Cloud Bridge service 
* Support for listing Amazon Web Services regions which are available for discovery and migration in the Cloud Bridge service 
* Support for model backup retention and restore in the Datascience service 
* Support for host capacity planning for host IO metrics in the Operations Insight service 
* Support for FastConnect redundancy in the Compute service 
* Support for create, publish, clone and delete operations on runbooks in the Fleet Application Management service 
* Support for platform configurations and metadata management in the Fleet Application Management service 
* Support for management of compliance policy rules in the Fleet Application Management service 
* Support for compliance report details based on compliance policy in the Fleet Application Management service 
* Support for administrative settings like auto discovery frequency in the Fleet Application Management service   

Changed 
------- 
* The vendored library PyJWT was upgraded from version `1.7.1` to version `2.4.0`   

Breaking 
-------- 
* The operation `update_plugin` was removed from the `OcbAgentSvcClient` client in the Cloud Bridge service 
* The property `discovery_schedule_id` was removed from the model `UpdateVmWareAssetSourceDetails` in the Cloud Bridge service 
* The constant `METRIC_NAME_HOST_CONTAINERS` and its value `HOST_CONTAINERS` was removed from the list of allowed values for the parameter `metric_name` in the model `HostPerformanceMetricGroup` in the Operations Insight service 
* The parent class of model `HostContainers` was changed from `HostPerformanceMetricGroup` to `HostConfigurationMetricGroup` and list of allowed values for the parameter `metric_name` was changed to `HOST_PRODUCT`, `HOST_RESOURCE_ALLOCATION`, `HOST_MEMORY_CONFIGURATION`, `HOST_HARDWARE_CONFIGURATION`, `HOST_CPU_HARDWARE_CONFIGURATION`, `HOST_NETWORK_CONFIGURATION`, `HOST_ENTITES`, `HOST_FILESYSTEM_CONFIGURATION`, `HOST_GPU_CONFIGURATION`, `HOST_CONTAINERS` in the Operations Insight service   

====================
2.136.0 - 2024-10-15
====================

Added 
----- 
* Support for open id connect discovery in the Oracle Kubernetes Engine service 
* Support for DNS security extensions (DNSSEC) in the DNS service 
* Support for restoring delta between backups to a new volume in the Block Volume service 
* Support for cross region backup copy and replication for volumes encrypted with customer keys in the Block Volume service 
* Support for list operation on deployment environments in the GoldenGate service 
* Support for defining environment types for deployments in the GoldenGate service   

Fixed 
----- 
* 

Fixed an issue with decoding UTF-8 characters in response models 
* Removed model files which were not accessible programmatically   

Breaking 
-------- 
* Response type changed to `oci.golden_gate.models.DeploymentBackup` for operations `copy_deployment_backup` and `create_deployment_backup` in the GoldenGate service   

====================
2.135.2 - 2024-10-08
====================

Added 
----- 
* Support for OCI Secure Desktops service 
* Support for window preferences on cloud automation tooling updates on ExaCC and ExaCS VM clusters in the Database service 
* Support for maintenance windows in the Stack Monitoring service 
* Renamed service OCI Container Engine to OCI Kubernetes Engine 
* Support for password as an optional parameter on creating admin users in the Fusion Apps as a Service 
* Support for IAM credentials for autonomous databases in the Operations Insights service   

Security 
------- 
* The upper bound for `cryptography` dependency has changed to versions less than `46.0.0`   

====================
2.135.1 - 2024-10-01
====================

Added 
----- 
* Support for calling Oracle Cloud Infrastructure services in the us-somerset-1 region 
* Support for calling Oracle Cloud Infrastructure services in the us-thames-1 region 
* Support for Security Attribute service
* Support for Zero Trust Packet Routing service 
* Support for zero trust packet routing security attributes in the Database service 
* Support for zero trust packet routing security attributes in the Networking service 
* Support for zero trust packet routing security attributes in the Network Load Balancer service 
* Support for disaster recovery failover in the Integration Cloud service   

====================
2.135.0 - 2024-09-24
====================

Added 
----- 
* Support for Generative AI Agent service 
* Support for undeleting autonomous databases in the Database service 
* Support for assigning key versions for the pluggable databases in the Database service 
* Support for lifecycle states on list autonomous database operation in the Database service 
* Support for data masking parameter on list refresh activity operation in the Fusion Application as a Service 
* Support for configuring custom endpoints on an instance in the Integration Cloud service 
* Support for updating channel schedules on instance create operation in the Analytics service 
* Support for ExaCC via management agents in the Operations Insights service 
* Support for appending and deleting allowed SQLs from SQL firewall policies in the Data Safe service 
* Support for alarm suppressions with compartment targets and recurring schedules in the Monitoring service   

Breaking 
-------- 
* A new value called `UNKNOWN_ENUM_VALUE` has been added to the enums of the parent class when a subclass is in the responses returned from services. If a service returns a value that cannot be recognized by the version of the SDK, then the enum will be set to this value. Previously this would throw an exception. 
* Property `dimensions` changed from required to optional in model `AlarmSuppressionSummary` in the Monitoring service 
* Value `STANDBY` was removed from the property `lifecycle_state` in models `IntegrationInstance` and `IntegrationInstanceSummary` in the Integration Cloud service   

====================
2.134.0 - 2024-09-17
====================

Added 
----- 
* Support for calling Oracle Cloud Infrastructure services in the eu-crissier-1 region 
* Support for dedicated AI cluster unit shapes in the Generative AI service 
* Support for ticket numbers when creating access requests in the Managed Access service 
* Support for 23ai database, cloud VM clusters and VM cluster patching in the Exadata Fleet Update service 
* Support for text to speech feature in the AI Speech service 
* Support for notifications and transfer of capacity requests in the OCI Control Center service   

Breaking 
-------- 
* Parameter `occ_customer_group_id` is now mandatory for methods `list_internal_namespace_occ_overviews`, `list_occ_availability_catalogs_internal`, `list_occ_capacity_requests_internal` in the OCI Control Center service  
2.133.0 - 2024-08-27
====================

Added 
----- 
* Support for Delegate Access Control service 
* Support for upgrade and downgrade of shapes of high performance mount targets in the File Storage service 
* Support for private endpoints in the Object Storage service 
* Support for create, update, list and delete operations on scheduling policies and scheduling windows in the Database service 
* Support for specifying domains while creating data guard associations in the Database service 
* Support for provision of developer autonomous databases in the Database service 
* Support for upgrade of developer autonomous databases to paid autonomous databases in the Database service 
* Support for scheduling plans, actions, execution windows and execution actions for maintenance scheduling in the Database service 
* Support for cross-region replication of virtual vaults in the Key Management service 
* Support for listing all active service summaries in the Announcements service 
* Support for VMware major and minor version upgrades in VMware Solution service 
* Support for updating protected database subscriptions in the Autonomous Recovery service 
* Support for health insurance id as an allowed document type in the Document Understanding service 
* Support for advanced database management features for autonomous databases in the Database Management service 
* Support for propagating request ids to load balancer servers in the Load balancer service 
* Support for automatic update orders in Fusion Application as a Service   

Breaking 
-------- 
* Constant `DOCUMENT_TYPE_INSURANCE_CLAIM` was renamed to `DOCUMENT_TYPE_HEALTH_INSURANCE_ID` in models `AnalyzeDocumentDetails` and `GeneralProcessorConfig` in the Document Understanding service 
* Property `document_id` was removed from model `DetectedDocumentType` in the Document Understanding service 
* Property `tenancy_id` was removed from models `DocumentClassificationFeature` and `DocumentKeyValueExtractionFeature` in the Document Understanding service   

====================
2.132.0 - 2024-08-20
====================

Added 
----- 
* Support for Fleet Application Management service 
* Support for creating maintenance runs using autonomous database software images in the Database service 
* Support for Object Storage buckets, Oracle databases, Oracle databases on exascale Infrastructure, autonomous container databases, and autonomous container databases on Cloud at Customer in the Disaster Recovery service 
* Support for multiple sharing modes in the OCI Cache service 
* Support for extended data retention periods for instances in the Integration Cloud service 
* Support for SQL watch and lifecycle management in the Database management service 
* Support for identity domains and feature sets in the Analytics Cloud service 
* Support for automatically extending the storage space for MySQL DB systems in pre-defined increments in the MySQL Database service   

Breaking 
-------- 
* Enums `protocol` in model `BasicDatabaseConnectionStringDetails`, `connector_type` in model `ConnectorDetails` and `DatabaseConnectionStringDetails`, `license_model` in model `DatabaseDiagnosticsAndManagementFeatureConfiguration`, `feature_status` in model `DatabaseFeatureConfiguration` in the Database management service will now follow forward compatibility rules - https://docs.oracle.com/en-us/iaas/tools/python/latest/forward-compatibility.html instead of raising `ValueError` for unknown enum values 
* The property `dr_plan_execution_type` has been removed from the API `list_dr_plan_executions` in the Disaster Recovery service   

====================
2.131.1 - 2024-08-13
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the me-abudhabi-4 region
* Support for viewing subscription limits in the Limits service
* Support for TCP idle timeout on network load balancer create and update operations in the Network Load Balancing service
* Support for creating integration instances of type Healthcare in the Integration Cloud service

Changed
-------
* The upper-bound for the circuitbreaker library was updated from `2.0.0` to `3.0.0` for Python versions 3.7 and above

====================
2.131.0 - 2024-08-06
====================

Added 
----- 
* Support for calling Oracle Cloud Infrastructure services in the me-riyadh-1 region 
* Support for vertically scaling a Database system in the PostgreSQL service 
* Support for flex shapes in the PostgreSQL service 
* Support for new fork repository feature in the Source Code Management service 
* Support for Developer Charts in the Source Code Management service 
* Support for pull requests and merge in Source Code Management service 
* Support for limiting custom and versioned custom software source content to the latest package versions in the OS Management service 
* Support for Open Data Hub (ODH) patching in a staged manner in the Big Data service 
* Support for Autoscale Memory Utilization in the Big Data service 
* Support for Resource Principal configuration feature in the Big Data service 
* Support for a new optional parameter compartment ID in the Java Management service 
* Support for Agent Installer in the Java Management service 
* Support for Java migration analysis request of deployed applications in the Java Management service 
* Support for JmsPlugin in the Java Management service 
* Support for improved cryptographic analysis result listing in the Java Management service 
* Support for improved fleet agent configuration setting in the Java Management service 
* Support for improved Java migration analysis result listing in the Java Management service 
* Support for improved library usage summary in the Java Management service 
* Support for improved performance tuning analysis result listing in the Java Management service 
* Support for improved work request listing in the Java Management service   

Breaking 
-------- 
* Parameter `credentials` is now required for model `CreateDbSystemDetails` in the PostgreSQL service   

====================
2.130.0 - 2024-07-30
====================

Added 
----- 
* Support for cluster placement groups on get operations in the Database service 
* Support for baseline metric for imported resources and metric extensions in the Stack Monitoring service 
* Support for implicit JIT and group membership provisioning during OpenID connect flow in the Identity Domains service 
* Support for realtime speech and customizations in the AI Speech service 
* Support for self-service instance maintenance API in the Compute service
* Support for GoldenGate suspend phase in the Database Migration service 
* Support for creating custom alert policies in the Data Safe service 
* Support for tunnel inspection in the Network firewall service 
* Support for diagnostics collection preferences and custom GI images in the Exadata Fleet Update service 
* Support for Resource Principals v2.1.2   

Breaking 
-------- 
* Property `service_principals` was removed from model `IdentityPropagationTrust` in the Identity Domains service   

====================
2.129.4 - 2024-07-23
====================

Added
-----
* Support for subscription id attribute in Cloud Exadata Infrastructure and Cloud VM Clusters in the Database service 
* Support for SQL and FTP monitors on create and update operations in the Application Performance Monitoring service 
* Support for MySQL Heatwave database systems in the Operations Insights service 
* Support for creating and updating schedules for user assessments and security assessments in the Data Safe service 
* Support for creating and updating sensitive data models of the tables for discovery in the Data Safe service 
* Support for additional optional parameters on autonomous database create and update operations in the Database service

Changed
-------
* The `INSTANCE_METADATA_URL_CERTIFICATE_RETRIEVER_RETRY_STRATEGY` was changed to retry a max of 3 times for max of 3 minutes and a fixed retry interval of 30 seconds, and retry on 404, 429 and 5xx errors

====================
2.129.3 - 2024-07-16
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the me-abudhabi-2 region
 
====================
2.129.2 - 2024-07-09
====================

Added
-----
* Support for cost management of shared resources in the Usage service
* Support for creating new databases with oracle key vault on Exadata Cloud at Customer in the Database service
* Support for confirming key store details on Exadata Cloud at Customer in the Database service
* Support for Download Manager in the Object Storage service

====================
2.129.1 - 2024-07-02
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the `ap-singapore-2` region
* Support for additional parameters in list and delete operations in the File Storage service
* Support for host capacity planning to analyze disabled and deleted resources in the Operations Insights service
* Support for title and description updates in the Capacity Management service
* Support for listing parameters for migrations in the Database Migration service
* Support for Oracle exadata database service on exascale Infrastructure (ExaDB-XS) in the Database service
 
====================
2.129.0 - 2024-06-25
====================

Added
-----
* Support for MySQL to MySQL homogeneous migrations in the Database Migration service
* Support for manual cross-region backups in the MySQL Heatwave service
  
Breaking
--------
* The models AdvisorSettings, Agent, AgentCollection, AgentImageCollection, AgentImageSummary, AgentSummary, AwsS3DataTransferMediumDetails, AwsS3Details, ChangeAgentCompartmentDetails, ConnectDescriptor, CreateAdvisorSettings, CreateAwsS3Details, CreateConnectDescriptor, CreateDataPumpSettings, CreateDataTransferMediumDetails, CreateDatabaseLinkDetails, CreateDumpTransferDetails, CreateGoldenGateDetails, CreateGoldenGateHub, CreateGoldenGateServiceDetails, CreateGoldenGateServiceDetails, CreatePrivateEndpoint, CreateSshDetails, CreateVaultDetails, DataPumpSettings, DataTransferMediumDetails, DataTransferMediumDetailsV2, DatabaseCredentials, DatabaseLinkDetails, DatabaseObject, DbLinkDataTransferMediumDetails, DumpTransferDetails, GoldenGateDetails, GoldenGateHub, GoldenGateServiceDetails, GoldenGateSettings, MigrationObjectSummary, NfsDataTransferMediumDetails, ObjectStorageDataTransferMediumDetails, PrivateEndpointDetails, SshDetails, UpdateAdvisorSettings, UpdateAgentDetails, UpdateAwsS3Details, UpdateConnectDescriptor, UpdateDataPumpSettings, UpdateDataTransferMediumDetails, UpdateDatabaseLinkDetails, UpdateDumpTransferDetails, UpdateGoldenGateDetails, UpdateGoldenGateHub, UpdateGoldenGateServiceDetails, UpdateGoldenGateSettings, UpdatePrivateEndpoint, UpdateSshDetails, UpdateVaultDetails, VaultDetails were removed in the Database Migration service
* The operations change_agent_compartment, delete_agent, get_agent, list_agent_images, list_agents, and update_agent were removed in the Database Migration service
* The composite operations delete_agent_and_wait_for_state and update_agent_and_wait_for_state were removed in the Database Migration service
* The properties `agent_id`, `source_container_database_connection_id`, `exclude_objects`, `include_objects` and `vault_details` were removed from the model `CloneMigrationDetails` in the Database Migration service
* The properties `admin_credentials`, `connect_descriptor`, `certificate_tdn`, `credentials_secret_id`, `database_id`, `database_type`, `is_dedicated`, `manual_database_sub_type`, `private_endpoint`, `replication_credentials`, `ssh_details` and `vault_details` were removed in the model `Connection` in the Database Migration service
* The properties `database_id`, `database_type`, `is_dedicated`, and `manual_database_sub_type` were removed in the model `ConnectionSummary` in the Database Migration service
* The properties `admin_credentials`, `certificate_tdn`, `connect_descriptor`, `database_id`, `database_type`, `manual_database_sub_type`, `private_endpoint`, `replication_credentials`, `ssh_details`, `tls_keystore`, `tls_wallet` and `vault_details` were removed from the model `CreateConnectionDetails` in the Database Migration service
* The properties `advisor_settings`, `agent_id`, `csv_text`, `data_transfer_medium_details`, `data_transfer_medium_details_v2`, `datapump_settings`, `dump_transfer_details`, `exclude_objects`, `golden_gate_details`, `golden_gate_service_details`, `include_objects`, `source_container_database_connection_id` and `vault_details` were removed in the model `CreateMigrationDetails` in the Database Migration service
* The properties `map_parallelism`, `max_apply_parallelism`, and `min_apply_parallelism` were removed in the models `Replicat`, `UpdateReplicat`, and `CreateReplicat` in the Database Migration service
* The properties `advisor_settings`, `agent_id`, `credentials_secret_id`, `data_transfer_medium_details`, `data_transfer_medium_details_v2`, `datapump_settings`, `dump_transfer_details`, `exclude_objects`, `golden_gate_details`, `golden_gate_service_details`, `include_objects`, `source_container_database_connection_id` and `vault_details` were removed in the model `Migration` in the Database Migration service
* The properties `csv_text` and `items` were removed in the model `MigrationObjectCollection` in the Database Migration service
* The properties `agent_id`, `source_container_database_connection_id` and `vault_details` were removed in the model `MigrationSummary` in the Database Migration service
* The properties `admin_credentials`, `certificate_tdn`, `connect_descriptor`, `database_id`, `private_endpoint`, `replication_credentials`, `ssh_details`, `tls_keystore`, `tls_wallet` and `vault_details` were removed from the model `UpdateConnectionDetails` in the Database Migration service
* The properties `advisor_settings`, `agent_id`, `data_transfer_medium_details`, `data_transfer_medium_details_v2`, `datapump_settings`, `dump_transfer_details`, `exclude_objects`, `golden_gate_details`, `golden_gate_service_details`, `include_objects`, `source_container_database_connection_id` and `vault_details` were removed in the model `UpdateMigrationDetails` in the Database Migration service
* Allowed values `ODMS_VALIDATE_GG_SERVICE` and `ODMS_INITIALIZE_GGS` were removed from property `wait_after` in the models `StartMigrationDetails` and `ResumeJobDetails` in the Database Migration service
* Allowed values `ODMS_VALIDATE_GG_SERVICE` and `ODMS_INITIALIZE_GGS` were removed from property `current_phase` in the model `MigrationJobProgressResource` in the Database Migration service
* Allowed values `ODMS_VALIDATE_GG_SERVICE` and `ODMS_INITIALIZE_GGS` were removed from property `current_phase` in the model `MigrationJobProgressSummary` in the Database Migration service
* Allowed values `ODMS_VALIDATE_GG_SERVICE` and `ODMS_INITIALIZE_GGS` were removed from property `name` in the models `MigrationPhaseSummary` and `PhaseStatus` in the Database Migration service
* Allowed values `ODMS_VALIDATE_GG_SERVICE` and `ODMS_INITIALIZE_GGS` were removed from property `wait_after` in the model `Migration` in the Database Migration service
 
====================
2.128.2 - 2024-06-18
====================

Added
-----
* Support for public connection urls and public endpoints for autonomous databases in the Database service
* Support for insurance claim document type in the AI Document service
* Support for Microsoft IIS discovery and monitoring in the Stack Monitoring service
 
====================
2.128.1 - 2024-06-11
====================

Added
-----
* Support for 23ai based databases in Globally Distributed Database service
* Support for testing span enrichment groups in Application Performance Monitoring service
* Support for subscription suspension and termination orders in Fusion Apps as a Service
* Support for time first occurred and time last occurred for resource sightings in Cloud Guard service
* Support for alarm summary, notification title, and slack duration on create and update operations in Monitoring service
* Support for message creation timestamp in Queue service
 
====================
2.128.0 - 2024-06-04
====================

Added
-----
* Support for creating cross-region autonomous data guards in the Database service
* Support for listing autonomous database peers in the Database service
* Support for dedicated AI clusters in the Generative AI service
* Support for Llama chat and Lora Fine-Tuning method in the Generative AI service
* Support for adding and removing locks for connections, deployments, and deployment backups in the GoldenGate service
* Support for additional connection types for deployments and connections in the GoldenGate service
 
Breaking
--------
* The possible allowed values `OPENAI` and `DALLE3` were removed from the property runtime_type in the models LlmInferenceResponse, CohereLlmInferenceResponse, and LlamaLlmInferenceResponse in the Generative AI service
* The property message was removed from the model CohereMessage in the Generative AI service
* The property chat_request was made required in the model ChatDetails in the Generative AI service
 
====================
2.127.0 - 2024-05-28
====================

Added
-----
* Support for Demand Signal service
* Support for external database connectors in the Database service
* Support for monitoring standby databases in the Database Management service
* Support for resource overviews in the Capacity Management service
* Support for optional parameters in the download API in the Java Management Service Downloads service
 
Breaking
--------
* The operation list_occ_availabilities can return any string for the params resource_type and workload_type in the OCI Control Center service
* The model OccCapacityRequestComputeDetails has been removed in the OCI Control Center service
* The params resource_type and workload_type can accept any string in the models OccAvailabilitySummary and OccCapacityRequestBaseDetails in the OCI Control Center service
 
====================
2.126.4 - 2024-05-21
====================

Added
-----
* Support for the Resource Scheduler service
* Support for Bring Your Own Container (BYOC), custom networking and graceful termination of pipelines in the Data Science service
* Support for backup and replacement of master, utility, and edge nodes in the Big Data service
* Support for nested resource principal in the Data Science service
 
====================
2.126.3 - 2024-05-14
====================

Added
-----
* Support for the Marketplace Private Offer service
* Support for resizing local file systems in the Database service
* Support for PPv2 (Proxy Protocol version 2) in the Load Balancer service
* Support for custom return path for sent emails in the Email Delivery service
* Support for session resumption in the Load Balancer service
 
====================
2.126.2 - 2024-05-07
====================

Added
-----
* Support for resizing of local file systems in the Database service
* Support for adding user defined pause group in disaster recovery plan in the Disaster Recovery service
* Support for OS patching configs in the Big Data service
* Support for IP inventory and notification feature in the Networking service
* Support for accidental delete protection for load balancers, load balancer listeners, and load balancer backends in the Load Balancer service
* Support for backend max connections for load balancers in the Load Balancer service
* Support for listener max connections for load balancers in the Load Balancer service
 
====================
2.126.1 - 2024-04-30
====================

Added
-----
* Support for enabling unified auditing for DBHome in the Database service
* Support for listing minor Grid Infrastructure (GI) versions available for custom GI software image creation in the Database service
* Support for network security groups in the Recovery Cloud service
* Support for lineage metadata import in the Data Catalog service
* Support for workspace properties in workspace create and update operations in the Data Integration service
* Support for monitoring ExaCC databases in the Database Management service
* Support for validations on target and policy before the masking process in the Data Safe service
 
====================
2.126.0 - 2024-04-23
====================

Added
-----
* Support for the Cluster Placement Groups service
* Support for new optional parameter for managing approval template in the Managed Access service
* Support for cluster placement groups in the Compute service
* Support for replacing boot volume for virtual machines in the Compute service
* Support for assigning a cluster placement group to boot and block volumes in the Block Storage service
* Support for container workload integration in the Cloud Guard service
* Support for instances in OCI and 3rd party clouds in the OS Management service
 
Breaking
--------
* Support for default retries on the operations of the Managed Access service
* The Application Migration service was decommissioned and removed
* The property `instance_location` was removed from the method `get_managed_instance_analytic_content` and `summarize_managed_instance_analytics` in the `ReportingManagedInstanceClient` in the OS Management service
* The property `display_name` was removed from the method `list_software_packages` in the `SoftwareSourceClient` in the OS Management service
* The property `AdvisoryType` was removed from the method `list_managed_instance_errata` in the `ManagedInstanceClient` in the OS Management service
* The type of property `Architecture` was changed from `string` to `SoftwarePackageArchitecture` in the models `SoftwarePackage` and `SoftwarePackageSummary` in the OS Management service
 
====================
2.125.3 - 2024-04-16
====================

	
Added
-----
* Support for calling Oracle Cloud Infrastructure services in the me-abudhabi-3 region
* Support for new Image resource for an Autonomous Database in the Database service
* Support for creating Autonomous Container Database using Autonomous Database Software Image in the Database service
* Support for new dedicated AI cluster unit shape in the Generative AI service
* Support for Chat API for LLM models in the Generative AI service
* Support for network security groups (NSGs) in the Redis service
* Support for custom public egress on model deployments in the Data Science service
* Support for a new data transfer parameter for AWS S3 bucket in the Database Migration service
* Support for Oracle Process Automation instance start and stop operations in the Process Automation service
* Support for healthcare Natural Language Processing (NLP) in the AI Language service
* Support for identification and de-identification of Private Health Information (PHI) service in the AI Language service
* Support for multilingual content for using machine learning models in the AI Language service
* Support for usage statements in cost management in the Usage service
 
====================
2.125.2 - 2024-04-09
====================

Added
-----

* Support for calling Oracle Cloud Infrastructure services in the ap-dcc-gazipur-1 region
* Support for the DNS-based backend health check in the Network Load Balancer service
* Support for Fail Open in the Network Load Balancer service
* Support for adding and updating Instant failover in the Network Load Balancer service
* Support for adding and updating source type and resource category for resource types in the Stack Monitoring service
* Support for searching resources based on resource category,  source type, multiple compartments, multiple lifecycle states in the Stack Monitoring service
* Support for filtering listed resources based on lifecycle status in the Stack Monitoring service
* Support for creating tasks with new config parameters in the Stack Monitoring service
* Support for Composite Resource Principal integration in the Data Flow service



====================
2.125.1 - 2024-04-02
====================

Added
-----
* Support for assigned private IP and single stack IPV6 feature for Network Load Balancer Service
* Support for Configuration API in Email Delivery Service
* Support for the status field in creating data source resource for Cloud Guard Service
* Support for TLSv1.3 in Load Balancer Service
* Support for sending mails via HTTPS for Email Delivery Service
 
====================
2.125.0 - 2024-03-26
====================

Added
-----
- Support for creating and updating a refreshable clone with auto-refresh for an Autonomous Database in the Database service
- Support for symmetric hashing in the Network Load Balancer service
- Support for creating and deploying helm command specifications in the DevOps Service
- Support for uninstalling helm chart when deleting an Oracle Kubernetes Stage through the DevOps Service
- Support for collecting metrics and filter plugin with Unified Monitoring Agent (UMA) in the Logging service
- Support for reading logs from head position after agent restart in the Logging service
- Support for monitoring MySQL HeatWave clusters in Database Management Service
- Support for multiple severities in an alarm in the Monitoring service
 
Breaking
--------
- The properties `DisplayName` and `Description` were made required in the model `CreateUnifiedAgentConfigurationDetails` in the Logging service
- The property `RecordInput` was made required in the model `OperationalMetricsSource` in the Logging service
 
====================
2.124.2 - 2024-03-19
====================

Added
-----
* Support for standalone Oracle HTTP server discovery and monitoring in the Stack Monitoring service
* Support for attribute management for traces in the Application Performance Monitoring service
* Support for async jobs and document translations in the AI language service
 
====================
2.124.1 - 2024-03-12
====================

Added
-----
* Support for new development license type on dedicated infrastructure in the Database service
* Support for placement parameters on Autonomous Container Database create operation in the Database service
* Support for autoscaling on model deployment in the Data Science service
 
====================
2.124.0 - 2024-03-05
====================

Added
-----
* Support for Linux capabilities configuration for the containers in the Container Instances service
* Support for service platforms in the Oracle Store Platform Gateway service
* Support for whisper models and delete job operation in the Speech service
* Support for new SQL insight content types in news reports in the Operations Insights service
* Support for launching virtual machines with multiple volumes in the Compute service
 
Breaking
--------
* The property `CapacityPlanningResources` has been made optional in the model `NewsContentTypes` in the Operations Insights service
 
====================
2.123.0 - 2024-02-27
====================

Added
-----
* Support for specifying dialog version when creating skills entities in the Digital Assistant service
* Support for bulk creation of skill entities in the Digital Assistant service
* Support for training skill query entities in the Digital Assistant service
* Support for cascading delete of skill custom entities in the Digital Assistant service
* Support for creating autonomous dataguard associations in the Database service
* Support for auto generation of secrets in the Secret Management service
* Support for cluster placement groups in Cloud Exadata Infrastructure in the Database service
* Support for retrieving previous logs of the container in the Container Instances service
* Support for queue sources in the Connector Hub service
* Support for automatic key rotation in the Key Management Service
* Support for downloading operator activity reports and assignment healthchecks in the Operator Access Control service
* Support for operator requesting access in the future time in the Operator Access Control service
* Support for forwarding hypervisor logs in the Operator Access Control service
* Support for asynchronous data asset export in the Data Catalog service
* Support for launch with multiple volumes for virtual machines in the Compute Service
* Support for tagging in Database Management service
 
Breaking
--------
* Support for default retries on operations of the Connector Hub service
* Property `max_cpu_core_count` was removed from models `UpdateAutonomousDatabaseDetails`, `CreateRefreshableAutonomousDatabaseCloneDetails`, `CreateCrossRegionDisasterRecoveryDetails`, `CreateCrossRegionAutonomousDatabaseDataGuardDetails`, `CreateAutonomousDatabaseFromBackupTimestampDetails`, `CreateAutonomousDatabaseFromBackupDetails`, `CreateAutonomousDatabaseDetails`, `CreateAutonomousDatabaseCloneDetails`, `CreateAutonomousDatabaseBase`, `AutonomousDatabase`, `AutonomousDatabaseSummary` in the Database service
* Property `key_id` in model `CreateSecretDetails` is made required in the Vault service
* Model `DatabaseConnectionCredentailsByName` was renamed to `DatabaseConnectionCredentialsByName` in the Database service
 
====================
2.122.0 - 2024-02-20
====================


Added
-----
* Support for calling Oracle Cloud Infrastructure services in the me-dcc-doha-1 region
* Support for Secure Desktops service
* Support for enabling and disabling Simultaneous Multithreading (SMT) for virtual machines in the Compute service
* Support for Bring Your Own Container Jobs (BYOC v2) in the Data Science service
* Support for expanded language translation in the AI Language service
* Support for additional flags for ignoring transliteration and text length to be considered for determining dominant language in the AI Language service
 
Breaking
--------
* The model `PreTrainedPhiModelDetails` was removed in the AI Language service
* The field `system_tags` has changed type from `dict(str, object)` to `dict(str, dict(str, object))` in the models `endpoint`, `endpoint_summary`, `model`, `model_summary`, `project`, and `project_summary` in the AI Language service
 
====================
2.121.1 - 2024-02-13
====================

Added
-----
* Support for adding automatic backups during cross region operations and disaster recovery in the Autonomous Database service
* Support for overlapping CIDR in network path analyzer in the Virtual Network Monitoring service
* Support for additional attributes in entity and topology in the Log Analytics service
* Support for historic collection and log type while creating object collection rules in the Log Analytics service
* Support for position aware parsers in the Log Analytics service
* Support for filtering log sources, detection rules and scheduled tasks based on target service in the Log Analytics service
* Support for additional recall and release attributes in the Log Analytics service
* Support for opc-meta-properties header while uploading log events in the Log Analytics service
* Support for Generative AI Inference service
 
====================
2.121.0 - 2024-02-06
====================

Added
-----
* Support for the Globally Distributed Database service
* Support for secret auto-rotation in the Secret Management service
* Support for dedicated key management in the Key Management service
* Support for resource locking operations in the Digital Media service
* Support for data sources, including prometheus emitter, in the Management Agent service
* Support for Bring Your Own Certificates (BYOC) in the MySQL HeatWave Database service
 
Breaking
--------
* Models `MediaWorkflowJobFact`, `MediaWorkflowJobFactCollection` and `MediaWorkflowJobFactSummary` were removed from the Digital Media service
* Methods `get_media_workflow_job_fact` and `list_media_workflow_job_facts` were removed from the Digital Media service
 
====================
2.120.0 - 2024-01-30
====================

Added
-----
* Support for OCI Control Center service
* Support for giro value set for address rules in the Oracle Store Platform service
* Support for giro in tax information for subscriptions in the Oracle Store Platform service
* Support for REST connectivity with Oath2 in the Data Integration service
* Support for resolver rules limit increase in the DNS service
* Support for named credentials in the Database Management service
 
Breaking
--------
* Default retry disabled on the operations of the DNS service
 
====================
2.119.1 - 2024-01-23
====================

Added
-----
* Support for the Generative AI service
* Support for additional currencies and countries for paid listings in the Marketplace service
* Support for process sets in the Stack Monitoring service
 
====================
2.119.0 - 2024-01-16
====================

Added
-----
* Support for resource id filter on the service work requests in the Container Instances service
* Support for polyglot vulnerability audit in the Application Dependency Management service
* Support for create, read, and update operations on peer databases in the Data Safe service
* Support for dimension specific alarm suppressions in the Monitoring service
* Support for calculating audit volume in the Data Safe service
* Support for viewing schema accesses in data safe user assessments in the Data Safe service
* Support for security feature usage in the Data Safe service
* Support for viewing the top security findings in data safe security assessments in the Data Safe service
* Support for additional filters in list findings operation in the Data Safe service
* Support for updating risk level of the specified finding in the Data Safe service
 
Breaking
--------
* Method `create_vulnerability_audit_and_wait_for_state` now waits on `oci.adm.models.VulnerabilityAudit` instead of `oci.adm.models.WorkRequest` in the Application Dependency Management service
 
====================
2.118.2 - 2024-01-11
====================

Fixed
-----
* Removed dependency on python-pkcs11
 
====================
2.118.1 - 2024-01-09
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the sa-valparaiso-1 region
* Support for creation of up to 60 containers per container instance in the Container Instances service
* Support for Oracle GoldenGate discovery and monitoring in the Stack Monitoring service
* Support for GoldenGate stream analytics in the GoldenGate service
* Support for backup work requests in MySQL Heatwave service
* Support for create, update, delete and list operations on premise vantage points in the Application Performance Monitoring service
* Support for create, update, delete and list operations on workers in the Application Performance Monitoring service
* Support for host capacity planning for compute instances and host unallocated metrics in the Operations Insights service
 
====================
2.118.0 - 2023-12-12
====================

Added
-----
* Support for changing compartments of configurations in the PostgreSQL service
* Support for granular policies including compartments, resource types, and recommendations in the Optimizer service
* Support for token exchanges in the Identity Domains service
* Support for Apache HTTP server discovery and monitoring in the Stack Monitoring service
* Support for resource locking in the Data Catalog service
* Support for concurrency throttling in the Data Integration service
* Support for reboot migrations for VMs on dedicated hosts in the Compute service
* Support for connection routing method settings and subnet update in the GoldenGate service
* Support for data discovery of commonly used sensitive types in the Data Safe service
* Support for incremental extract and updates to the workflows in the Data Integration service 
 
Breaking
--------
* Support for default retries on the operations of the Optimizer service
 
====================
2.117.0 - 2023-12-04
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the eu-dcc-zurich-1 and the sa-bogota-1 region
* Support for managing certificates of target Servers in the Golden Gate service
* Support for AWR Hub Snapshot ingest endpoints in the Operations Insights service
* Support for reducing false positives in the Application Dependency Management service
* Support for ARM shapes in the Data Science service
* Support for new optional parameters in the upload discovery data API in the Usage service
* Support for multiple clusters in a Software-Defined Data Centers (SDDCs) in the Ocvp service
* Support for No/Zero days backup in Autonomous Container Database in the Database service
* Support for provisioning a VM Cluster with a choice of Exadata image version in the Database service
* Support for updating ocpu/ecpu count, local storage , ACD count and Exadata storage on Cloud Autonomous VM Cluster and Autonomous VM Cluster in the Database service
* Support for serial console history in the Database service
* Support for Oracle Linux 8 version database system in the Database service
 
Breaking
--------
* Constants `CURRENT_SKU_HOUR`, `CURRENT_SKU_MONTH`, `CURRENT_SKU_ONE_YEAR`, `CURRENT_SKU_THREE_YEARS`, `NEXT_SKU_HOUR`, `NEXT_SKU_MONTH`, `NEXT_SKU_ONE_YEAR`, `NEXT_SKU_THREE_YEARS` were renamed to `CURRENT_COMMITMENT_HOUR`, `CURRENT_COMMITMENT_MONTH`, `CURRENT_COMMITMENT_ONE_YEAR`, `CURRENT_COMMITMENT_THREE_YEARS`, `NEXT_COMMITMENT_HOUR`, `NEXT_COMMITMENT_MONTH`, `NEXT_COMMITMENT_ONE_YEAR`, `NEXT_COMMITMENT_THREE_YEARS` respectively in models `CreateEsxiHostDetails`, `EsxiHost` and `EsxiHostSummary` in the Ocvp service
* Parameters `sddc_id`, `current_sku`, `next_sku`, were renamed to `cluster_id`, `current_commitment`, `next_commitment` in models `CreateEsxiHostDetails`, `EsxiHost` and `EsxiHostSummary` in the Ocvp service
* Parameters `non_upgraded_esxi_host_id` and `failed_esxi_host_id` were removed from model `CreateEsxiHostDetails` in the Ocvp service
* Constants `INITIAL_SKU_HOUR`, `INITIAL_SKU_MONTH`, `INITIAL_SKU_ONE_YEAR`, `INITIAL_SKU_THREE_YEARS` were removed from model `CreateSddcDetails` in the Ocvp service
* Parameters `compute_availability_domain`, `instance_display_name_prefix`, `esxi_hosts_count`, `initial_sku`, `is_hcx_enabled`, `hcx_vlan_id`, `is_hcx_enterprise_enabled`, `workload_network_cidr`, `provisioning_subnet_id`, `vsphere_vlan_id`, `vmotion_vlan_id`, `vsan_vlan_id`, `nsx_v_tep_vlan_id`, `nsx_edge_v_tep_vlan_id`, `nsx_edge_uplink1_vlan_id`, `nsx_edge_uplink2_vlan_id`, `replication_vlan_id`, `provisioning_vlan_id`, `initial_host_shape_name`, `initial_host_ocpu_count`, `is_shielded_instance_enabled`, `capacity_reservation_id`, `datastores` were removed from model `CreateEsxiHostDetails` in the Ocvp service
* Models `SupportedSkuSummary` and `SupportedSkuSummaryCollection` were removed from the Ocvp service
 
====================
2.116.0 - 2023-11-14
====================

Added
-----
* Support for the PostgreSQL service
* Support for new operations in the Identity Domains service
* Support for enabling, disabling, and renewing SSL/TLS in the Big Data service
* Support for diarization in the AI Speech service
* Support for Capacity Topology API in the Compute service  
 
Breaking
--------
* Model `MyRequest` in the Identity Domains service now allows only certain restricted values. For more information please see https://docs.public.oneportal.content.oci.oraclecloud.com/en-us/iaas/tools/python/latest/api/identity_domains/models/oci.identity_domains.models.MyRequest.html#oci.identity_domains.models.MyRequest 
 
====================
2.115.1 - 2023-11-07
====================

Added
-----
* Support for Java Management Service Downloads
* Support for creating autonomous dataguard associations in the Database service
* Support for SaaS administrative user configurations for autonomous database in the Database service
* Support for macOS in the the Java Management service
* Support for distribution and management of deployment rule sets in the Java Management service
* Support for new download location of Oracle Java runtime binaries in the Java Management service
* Support for exporting data across regions in the Java Management service
 
Fixed
-----
* Fixed an issue in Resource Principals v2.1 introduced in the `v2.111.0` release
 
====================
2.115.0 - 2023-10-31
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the us-saltlake-2 region
* Support for disaster recovery of load balancers, network load balancers and file systems in the Disaster Recovery service
* Support for performing disaster recovery drills in the Disaster Recovery service
* Support for enterprise SKUs and extensibility in the Stack Monitoring service
* Support for metric extensions in the Stack Monitoring service
* Support for baseline and anomaly detection in the Stack Monitoring service
* Support for integration with Database Management service in the MySQL HeatWave service
* Support for MySQL database management in the Database Management service
* Support for database firewalls in the Data Safe service
 
Breaking
--------
* The properties `compartment_id` and `user_assessment_id` were removed from the `ProfileAggregation` model in the Data Safe service
 
====================
2.114.0 - 2023-10-24
====================

Added
-----
* Support for optional parameters for autonomous container database create and update operations in the Database service
* Support for maintenance runs for autonomous container database resources in the Database service
* Support for runtime unsupported connections for Oracle Database and MySQL database types in the Database Tools service
* Support for PostgreSQL, Generic JDBC connections with runtime unsupported in the Database Tools service
* Support for resource locking in the Database Tools service
* Support for proxy sessions for Oracle database connections in the Database Tools service
* Support for global active tables in the NoSQL Database service
* Support for application dependency management (ADM) remediation features in the Application Dependency Management service
* Support for additional connections types for Amazon Kinesis, Amazon Redshift, Elasticsearch, Generic, Google BigQuery, Google Cloud Storage and Redis Database resources in the Golden Gate service
* Support for optional parameters for the list alarms status operation in the Monitoring Service
 
Breaking
--------
* Support for retries by default on operations of the Database Tools service
* Support for retries by default on operations of the Monitoring service
* The parameter `opc_retry_token` was removed from operations `change_database_tools_connection_compartment` and `change_database_tools_private_endpoint_compartment` in the Database Tools service
* Properties `user_password`, `connection_string` and `user_name` were removed from models `CreateDatabaseToolsConnectionOracleDatabaseDetails` and `CreateDatabaseToolsConnectionMySqlDetails` in the Database Tools service
 
====================
2.113.0 - 2023-10-17
====================

Added
-----
* Support for the Caching Service
* Support for the Marketplace Publisher service
* Support for higher limits for network firewalls in the Network Firewall service
* Support for exporting access request reports in the Lockbox service
* Support for storage mounts for jobs and notebooks in the Data Science service
* Support for unified agent operational metrics for the service configurations in the Logging Management service
 
Breaking
--------
* Property `approver_levels` in models `ApprovalTemplateSummary` changed from required to optional in the Lockbox service
* Properties `lockbox_partner` and `partner_compartment_id` in models `LockboxSummary` changed from required to optional in the Lockbox service
* Allowed values `ENUM_STRING` and `RQS_FILTER` were removed from the property `type` in model `Parameter` in the Logging service
* Properties `rqs_type` and `display_name` were removed from model `Parameter` in the Logging service
* Parameter `service_stage` was removed from operation `list_services` from the logging management client in the Logging service
* Properties `mapped_secrets`, `application_lists`, `url_lists`, `ip_address_lists`, `security_rules`, `decryption_rules` and `decryption_profiles` were removed from models `CreateNetworkFirewallPolicyDetails`, `NetworkFirewallPolicy` and `UpdateNetworkFirewallPolicyDetails` in the Network Firewall Service
* Property `sources` is replaced by `source_address` and property `destinations` is replaced by `destination_address` in models `DecryptionRuleMatchCriteria` and `SecurityRuleMatchCriteria` in the Network Firewall Service
* Property `applications` is replaced by `application` and property `urls` is replaced by `url` in model `SecurityRuleMatchCriteria`in the Network Firewall Service
 
====================
2.112.4 - 2023-10-10
====================

Added
-----
* Support for creating flow log type capture filters in Virtual Cloud Network service
* Support for export and import of metadata in Data Integration service
* Support for displaying resource usage information on autonomous vm cluster get operations in Database service
* Support for displaying resource usage information for the list of autonomous container databases on autonomous vm cluster get operations in Database service
* Support for pluggable database with enhanced features in Database service
* Support for exporting container and kubernetes app listings in Marketplace service
* Support for work request statuses for export container and kubernetes app listings in Marketplace service
 
====================
2.112.3 - 2023-10-03
====================

Added
----- 
* Support for elastic resource pools in the Database service
* Support for private endpoints in the Data Science service
* Support for File System Service (FSS) as transfer medium for data export and import in the Database Migration service
* Support for new optional parameters on replica create, update and list operations in the MySQL Heatwave service  
 
====================
2.112.2 - 2023-09-26
====================

Added
-----
* Support for listing compute performances and storage performances in Database service
* Support for private endpoints for external key managers in Key Management service
* Support for additional parameters in vaults and keys for external key managers in Key Management service
* Support for domains while creating integration instances in Oracle Integration Cloud service

====================
2.112.1 - 2023-09-12
====================

Added
------
* Support for SQL tuning sets in Database Management service
* Support for announcement chaining in Announcements service
* Support for automatic promotion of hosts in Stack Monitoring service
* Support for face detection in AI Vision service
* Support for change parameters on list character sets operation in Database Management service
* Support for displaying software sources attached to a managed instance group in OS Management service
* Support for Alloy configuration
 
Fixed
-----
* Fixed a bug in `EnvRptPathProvider` introduced after adding support for Resource Principals v3
 
====================
2.112.0 - 2023-09-05
====================

Added
-----
* Support for queue channels in the Queue Service
* Support for entity lineage retrieval and asynchronous glossary export in the Data Catalog service
* Support for filtering and sorting while listing work requests in the Container Instances service
* Support for the ability to create support requests for various support ticket types (TECH, LIMIT, ACCOUNT) in the Customer Incident Management Service
* Endpoint changed from https://incidentmanagement.{region}.{domainAndTopLevelDomain} to https://incidentmanagement.{region}.oci.{domainAndTopLevelDomain} (e.g. https://incidentmanagement.us-phoenix-1.oraclecloud.com to https://incidentmanagement.us-phoenix-1.oci.oraclecloud.com) in the Customer Incident Management Service
 
Breaking
--------
* The models `UserClient` and `UserClientCompositeOperations` were removed in the Customer Incident Management Service
* The parameter `availability_domain` was removed from models `Resource` and `CreateResourceDetails` in the Customer Incident Management Service
* The constants `REGION_DEV`, `REGION_SEA`, `REGION_INTEG_NEXT`, `REGION_INTEG_STABLE`, `REGION_PHX`, `REGION_IAD`, `REGION_FRA`, `REGION_EU_FRANKFURT_1`, `REGION_LHR`, `REGION_YYZ`, `REGION_NRT`, `REGION_ICN`, `REGION_BOM`, `REGION_GRU`, `REGION_SYD`, `REGION_ZRH`, `REGION_JED`, `REGION_AMS`, `REGION_KIX`, `REGION_MEL`, `REGION_YUL`, `REGION_HYD`, `REGION_YNY` were removed from the models `Resource` and `CreateResourceDetails` in the Customer Incident Management Service
* The constants `AVAILABILITY_DOMAIN_DEV_1`, `AVAILABILITY_DOMAIN_DEV_2`, `AVAILABILITY_DOMAIN_DEV_3`, `AVAILABILITY_DOMAIN_INTEG_NEXT_1`, `AVAILABILITY_DOMAIN_INTEG_STABLE_1`, `AVAILABILITY_DOMAIN_SEA_AD_1`, `AVAILABILITY_DOMAIN_SEA_AD_2`, `AVAILABILITY_DOMAIN_SEA_AD_3`, `AVAILABILITY_DOMAIN_PHX_AD_1`, `AVAILABILITY_DOMAIN_PHX_AD_2`, `AVAILABILITY_DOMAIN_PHX_AD_3`, `AVAILABILITY_DOMAIN_US_ASHBURN_AD_1`, `AVAILABILITY_DOMAIN_US_ASHBURN_AD_2`, `AVAILABILITY_DOMAIN_US_ASHBURN_AD_3`, `AVAILABILITY_DOMAIN_US_ASHBURN_AD_4`, `AVAILABILITY_DOMAIN_EU_FRANKFURT_1_AD_1`, `AVAILABILITY_DOMAIN_EU_FRANKFURT_1_AD_2`, `AVAILABILITY_DOMAIN_EU_FRANKFURT_1_AD_3`, `AVAILABILITY_DOMAIN_UK_LONDON_1_AD_1`, `AVAILABILITY_DOMAIN_UK_LONDON_1_AD_2`, `AVAILABILITY_DOMAIN_UK_LONDON_1_AD_3`, `AVAILABILITY_DOMAIN_CA_TORONTO_1_AD_1`, `AVAILABILITY_DOMAIN_AP_TOKYO_1_AD_1`, `AVAILABILITY_DOMAIN_AP_SEOUL_1_AD_1`, `AVAILABILITY_DOMAIN_AP_MUMBAI_1_AD_1`, `AVAILABILITY_DOMAIN_SA_SAOPAULO_1_AD_1`, `AVAILABILITY_DOMAIN_ME_JEDDAH_1_AD_1`, `AVAILABILITY_DOMAIN_AP_OSAKA_1_AD_1`, `AVAILABILITY_DOMAIN_AP_SYDNEY_1_AD_1`, `AVAILABILITY_DOMAIN_EU_ZURICH_1_AD_1`, `AVAILABILITY_DOMAIN_EU_AMSTERDAM_1_AD_1`, `AVAILABILITY_DOMAIN_AP_MELBOURNE_1_AD_1`, `AVAILABILITY_DOMAIN_CA_MONTREAL_1_AD_1`, `AVAILABILITY_DOMAIN_AP_HYDERABAD_1_AD_1`, `AVAILABILITY_DOMAIN_AP_CHUNCHEON_1_AD_1`, `AVAILABILITY_DOMAIN_NO_AD` were removed from the models `Resource` and `CreateResourceDetails` in the Customer Incident Management Service
* The parameter `region` was modified to accept any string in the models `Resource` and `CreateResourceDetails` in the Customer Incident Management Service
* The parameter `country` was removed from the model `CreateUserDetails` in the Customer Incident Management Service
* The parameter `source` was removed from the operation `get_status` in `IncidentClient` the Customer Incident Management Service
 
====================
2.111.0 - 2023-08-29
====================

Added
----- 
* Support for creating and updating network monitors in the Application Performance Monitoring Synthetics service
* Support for integration of GoldenGate service for replication in the Database Migration Service
* Support for displaying resource usage information on autonomous container database and cloud autonomous vm cluster get operations in the Database service
* Support for FastConnect Media Access Control Security (MACSec) fail open option in the Network Monitoring service
* Support for generic bare metal types and configuration maps in compute instance platform configuration in the Compute service
* Support for encrypted FastConnect in the Network Monitoring service
* Support for new parameters on customer premises equipment and virtual circuit create operations in the Network Monitoring service
* Support for virtual circuit associated tunnels in the Network Monitoring service
* Support for additional parameters on dynamic routing gateway create and update operations in the Network Monitoring service
* Support for assigning an IPv6 address to a compute instance during instance launch or secondary VNIC attach in the Compute service
* Support for Resource Principals v3.0
* Support for OKE Workload Auth Provider
 
Breaking
--------
* Models `AddAnalyticsClusterDetails`, `AddHeatWaveClusterDetails`, `AnalyticsCluster`, `AnalyticsClusterMemoryEstimate`, `AnalyticsClusterNode`, `AnalyticsClusterSchemaMemoryEstimate`, `AnalyticsClusterSummary`, `AnalyticsClusterTableMemoryEstimate`, `UpdateAnalyticsClusterDetails` were removed from MySQL Database Service
* Parameters `is_analytics_cluster_attached` and `analytics_cluster` removed from models `DbSystemSummary` and `DbSystem`, in the MySQL Database Service
* Allowed values `ADD_ANALYTICS_CLUSTER`, `UPDATE_ANALYTICS_CLUSTER`, `DELETE_ANALYTICS_CLUSTER`, `START_ANALYTICS_CLUSTER`, `STOP_ANALYTICS_CLUSTER`, `RESTART_ANALYTICS_CLUSTER`, `GENERATE_ANALYTICS_CLUSTER_MEMORY_ESTIMATE` were removed from parameter `operation_type` from model `WorkRequest`, `WorkRequestSummary` in the MySQL Database Service
* Allowed value `ANALYTICSCLUSTER` was removed from parameter `is_supported_for` from model `ShapeSummary` in the MySQL Database Service
* Allowed value `ANALYTICSCLUSTER` was removed from parameter `is_supported_for` from operation `list_shapes` in the `mysqlaas_client` in the MySQL Database Service
* Operations `add_analytics_cluster`, `delete_analytics_cluster`, `generate_analytics_cluster_memory_estimate`, `get_analytics_cluster`, `get_analytics_cluster_memory_estimate`, `restart_analytics_cluster`, `start_analytics_cluster`, `stop_analytics_cluster`, `update_analytics_cluster` were removed from the `db_system_client` in the MySQL Database service
* Operations `add_analytics_cluster_and_wait_for_state`, `delete_analytics_cluster_and_wait_for_state`, `generate_analytics_cluster_memory_estimate_and_wait_for_state`, `restart_analytics_cluster_and_wait_for_state`, `start_analytics_cluster_and_wait_for_state`, `stop_analytics_cluster_and_wait_for_state`, `update_analytics_cluster_and_wait_for_state` were removed from client `db_system_client_composite_operations` in the MySQL Database service
 
====================
2.110.2 - 2023-08-22
====================

Added
-----
* Support for Compute Cloud at Customer service
* Support for warehouse data objects in the Operations Insights service
* Support for standard queries on operations Insights data objects in the Operations Insights service
* Support for database in memory on autonomous database create operations in the Database service
 
====================
2.110.1 - 2023-08-15
====================

Added
-----
* Support for credential stores, including Single Sign-On support, for deployments in the GoldenGate service
* Support for container security contexts in the Container Instances service
* Support for placement constraints and cluster configurations on cluster networks in the Compute service
2.110.0 - 2023-08-08
====================

Added
-----
* Support for backup retention on autonomous database create operations in the Database service
* Support for exclude tables for replication in the Database Migration service
* Support for adding and updating auto failover maximum data loss limits for local autonomous data guards in the Database service
* Support for limiting networking diagram ingestion in the Networking Monitoring service
* Support for new operations for deployment upgrades in the GoldenGate service
* Support for getting model type information and base model versions while creating language custom models in the AI Language service
* Support for support field in class metric in the AI Language service
* Support for Compute Cloud at Customer resource type in the Operator Access Control service
* Support for managing account management info, account recovery settings, app roles, apps, app status changers, grants, identity propagation trusts and settings, request-able groups, requests, security questions, OAuth tokens, and user attribute settings in the Identity Domains service

Breaking
--------
* Property `ipv6_cidr_block` is removed from models `Vcn` and `CreateVcnDetails` in the Networking Monitoring service
* Property `ipv6_public_cidr_block` is removed from models `Vcn` and `Subnet` in the Networking Monitoring service
* Property `is_internet_access_allowed` is removed from models `UpdateIpv6Details`, `Ipv6` and `CreateIpv6Details` in the Networking Monitoring service
* Property `public_ip_address` is removed from model `Ipv6` in the Networking Monitoring service
* Support for retries by default on operations of the Operator Access Control service

====================
2.109.0 - 2023-08-01
====================

Added
-----
* Support for the Exadata Fleet Update service
* Support for REST-based log collection, multi-conditional labels, and collection properties in the Logging Analytics service
* Support for Kubernetes cluster credential rotation in the Container Engine for Kubernetes service
* Support for zero-downtime features in the Fusion Apps as a Service service
* Support for news reports in the Operations Insights service 
 
Breaking
--------
* Allowed value `ACCELERATION_MAINTENANCE` was removed from the property `task_type` in the models `StandardTask`, `ScheduledTaskSummary` and `ScheduledTask` in the Logging Analytics service
* Allowed value `ACCELERATION_MAINTENANCE` was removed from the parameter `task_type` in operation `list_scheduled_tasks` in the Logging Analytics service
 
====================
2.108.0 - 2023-07-25
====================

Added
-----
* Support for composing multiple document service custom key value models into one single model in Document Understanding Service
* Support for custom hostname in the Compute service
* Support for cloud subscription in the Organizations service
* Support for automatic backup download in the GoldenGate service
* Support for creating single use (non-recurring) budgets in the Budgets service  
 
Breaking
--------
* Support for retries by default on operations of the Budgets service
* Properties `is_classic_subscription`, `payment_model`, `region_assignment`, `lifecycle_state`, `start_date`, `end_date`, `classic_subscription_id`, `time_created` are deleted from model `SubscriptionSummary` in the Organizations service
* Properties `classic_subscription_id`, `is_classic_subscription`, `payment_model`, `region_assignment`, `lifecycle_state`, `skus`, `program_type`, `customer_country_code`, `cloud_amount_currency`, `csi_number`, `subscription_tier`, `is_government_subscription`, `promotion`, `purchase_entitlement_id`, `start_date`, `end_date` are deleted from models `Subscription` and `AssignedSubscription` in the Organizations service
* Properties `classic_subscription_id`, `is_classic_subscription`, `payment_model`, `region_assignment`, `lifecycle_state`, `start_date`, `end_date`, `csi_number` are deleted from model `AssignedSubscriptionSummary` in the Organizations service
 
====================
2.107.0 - 2023-07-18
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the mx-monterrey-1 region
* Support for Kerberos and LDAP with NFSv3 in the File Storage service
* Support for capacity reservation checks for movable compute instances in the Disaster Recovery service
* Support for Oracle MFT monitoring in the Stack Monitoring service
* Support for OS patching in the Big Data service
* Support for master and utility nodes in the Big Data service
* Support for connectivity testing in the GoldenGate service
 
Breaking
--------
* The type of property `size_in_bytes` was changed from `float` to `int` for the `DeploymentBackup`, `DeploymentBackupSummary`, `TrailFileSummary`, and `TrailSequenceSummary` in the GoldenGate service
* The property `function_id` was made required in the model `UpdateInvokeFunctionUserDefinedStepDetails` in the Disaster Recovery service
* The properties `run_on_instance_id` and `script_command` were made required in the model `UpdateRunLocalScriptUserDefinedStepDetails` in the Disaster Recovery service
* The properties `run_on_instance_id` and `object_storage_script_location` were made required in the model `UpdateRunObjectStoreScriptUserDefinedStepDetails` in the Disaster Recovery service
* The property `additional_capabilities` was removed from models `CreateContainerDetails` and `Container` in the Container Instances service
 
====================
2.106.0 - 2023-07-11
====================

Added
-----
* Support for specifying default snapshot enablement, verified response codes, client certificate details, and request authentication schemes when creating or updating synthetic monitors in the Application Performance Monitoring service
* Support for address rules, address verification, and requesting addresses in the OSP Gateway service
* Support for synchronous operations in the Document Understanding service
* Support for migration without SSH to database hosts (DMS) in the Database Migration service
* Support for processing workload mappings in the Container Engine for Kubernetes service
* Support for Salesforce, MySQL HeatWave, and Oracle EBS, Sieble, and PeopleSoft connectors in the Data Integration service
* Support for updating the envelope key of a volume backup in the Block Volume service 
 
Breaking
--------
* Support for retries by default on operations of the OSP Gateway service
* The type of property `BillingAddress` was changed from `BillingAddress` to `Address` in the `Subscription` and `SubscriptionSummary` models in the OSP Gateway service
* Enums `value_type` in model `FieldValue`, `field_type` in model `DocumentField`, `unit` in model `Dimensions` will now follow forward compatibility rules - https://docs.oracle.com/en-us/iaas/tools/python/latest/forward-compatibility.html instead of raising `ValueError` for unknown enum values
 
Security
-------
* The upper bound for `cryptography` dependency has changed to versions less than `42.0.0`
 
====================
2.105.0 - 2023-06-27
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the eu-frankfurt-2 region
* Support for the OS Management Hub service
* Support for changing the key store type, and rotating keys, on Exadata Cloud at Customer in the Database service
* Support for launching VM database systems using Ampere A1 shapes in the Database service
* Support for additional currencies and countries on paid listings in the Marketplace service
* Support for ECPU integration in the License Manager service
* Support for freeform and defined tags on resources in the Generic Artifacts service
* Support for SQL endpoints in the Data Flow service
* Support for setting replication delays on channels in the MySQL Database service
* Support for setting how channels handle replicated tables with no primary key in the MySQL Database service
* Support for SQL Plan Management (SPM) in Database Management service  
 
Breaking
--------
* Support for retries by default on operations of the Generic Artifacts service
 
====================
2.104.3 - 2023-06-20
====================

Added
-----
* Support for serial console access in the Database service
* Support for an increased storage size limit of up to 384 TBs in the Database service
* Support for network security group (NSG) support for private database registrations / private endpoints in the Database Migration service
* Support for document classification on documents of more than one page in the Data Labeling service
* Support for importing datasets in the Data Labeling service
* Support for specifying a shape when creating applications in the Functions service
* Support for creating and managing pools in the Data Flow service
* Support for specifying certificate parameters when creating or updating a node in the Roving Edge Infrastructure service
* Support for certificate management in the Roving Edge Infrastructure service
* Support for upgrade bundle management in the Roving Edge Infrastructure service
 
====================
2.104.2 - 2023-06-13
====================

Added
-----
* Support for the OCI Control Center service
* Support for resource quotas and limits in the Usage service
* Support for allowing users to select the billing interval of deleted ESXi hosts while adding new ESXi hosts in the VMWare Solution service
* Support for custom key/value pairs and custom document classification in the AI Document service
* Support for namespace-prefixed domains in the Object Storage service
* Support for getting the full path to a pre-authenticated request in the Object Storage service
* Support for Java migration analysis, performance tuning recommendations, and JDK LCM customization in the Java Management service
* Support for the TCPS protocol for cloud databases in the Operations Insights service
* Support for AIX hosts that are monitored via Enterprise Manager in the Operations Insights service
 
====================
2.104.1 - 2023-06-06
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the eu-madrid-2 region
* Support for bulk include/exclude of migration objects in the Database Migration service
* Support for Kafka cluster profiles, including dedicated Kafka broker nodes, in the Big Data service
* Support for MySQL HeatWave Lakehouse in the MySQL Database service
* Support for capacity reports in the Compute service

====================
2.104.0 - 2023-05-30
====================

Added
-----
* Support for policy-based snapshots in the File Storage service
* Support for creating and updating a VM cluster network with disaster recovery network support in the Database service
* Support for setting a management dashboard or saved search to be shared across OCI Observability & Management services in the Management Dashboard service  
 
Breaking
--------
* The property `port` was deprecated and made optional in the `ScanDetails` model in the Database service
 
====================
2.103.0 - 2023-05-23
====================

Added
-----
* Support for CRI-O parsing in the Logging service
* Support for retrieving the resource availability domain when getting Exadata infrastructure or VM clusters in the Database service
* Support for specifying database servers when creating dedicated autonomous databases in the Database service
* Support for secondary egress zones in the DNS service
 
Breaking
--------
* The models `LogIncludedSearch`, `LogIncludedSearchSummary`, `LogIncludedSearchSummaryCollection`, `LogIncludedSearch`, `LogIncludedSearchSummary` and `LogIncludedSearchSummaryCollection` were removed in the Logging service
* The property `keys` was made required in the `UnifiedAgentCsvParser` and `UnifiedAgentTsvParser` models in the Logging service
* The property `patterns` was made required in the `UnifiedAgentGrokParser` and `UnifiedAgentMultilineGrokParser` models in the Logging service
* The properties `sources` and `destination` were made required in the `UnifiedAgentLoggingConfiguration` model in the Logging service
* The property `format` was made required in the `UnifiedAgentMultilineParser` model in the Logging service
* The property `expression` was made required in the `UnifiedAgentRegexParser` model in the Logging service
* The property `paths` was made required in the `UnifiedAgentTailLogSource` model in the Logging service
* The property `channels` was made required in the `UnifiedAgentWindowsEventSource` model in the Logging service
* The operations `get_log_included_search` and `list_log_included_searches` were removed from the `LoggingManagementClient` in the Logging service
* A new required property `external_downstreams` was added in the `zone` model in the DNS service
 
====================
2.102.0 - 2023-05-16
====================

Added
-----
* Support for self-service integration in the Fusion Apps as a Service service
 
Breaking
--------
* The models `AttachExistingInstanceDetails`, `CreateNewInstanceDetails`, `CreateOicServiceInstanceDetails`, `CreateServiceInstanceDetails`, `FawAdminInfoDetails` and `CreateOaxServiceInstanceDetails` were removed from the Fusion Apps as a Service service
* The property `action` was removed from the `ServiceAttachment` model in the Fusion Apps as a Service service
* The property `action` was removed from the `CreateServiceAttachmentDetails` model in the Fusion Apps as a Service service
 
====================
2.101.0 - 2023-05-09
====================

Added
-----
* Support for the Access Governance service
* Support for creating, updating, listing and downloading one-off patches in the Database service
* Support for changing disaster recovery configurations of remote autonomous databases in the Database service
* Support for scheduling automatic backups in the Database service
* Support for provisioning Software-Defined Data Centers (SDDCs) using standard bare metal shapes, with Block Storage as the datastore, in the VMWare Solution service
* Support for parity with the configuration options of the Compute service in the Compute Autoscaling service
 
Breaking
--------
* The Data Connectivity Management service was removed from the SDK
 
====================
2.100.0 - 2023-05-02
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the eu-jovanovac-1 region
* Support for bring-your-own-license TLS and ORDS certificates in the Database service
* Support for tags in the Stack Monitoring service
* Support for GPU shapes for model deployments in the Data Science service
* Support for returning networking details of instances in the Visual Builder service
* Support for high-memory VMs in the Compute service
* Support for integrating with the Integration Cloud service in the Process Automation service
* Support for managing on-demand node upgrades in node pools in the Container Engine for Kubernetes service  
 
Breaking
--------
* The model `UpdateVirtualNodeDetails` was removed from the Container Engine for Kubernetes service
* The property `type` in the `DiscoveryDetails` model in the Application Migration service was fixed to no longer support `UNKNOWN_ENUM_VALUE`. Instead, a `ValueError` will be raised if this property is assigned a value that it does not support.
* The property `protocol` in the `IdentityProvider` model in the Identity Data Plane service was fixed to no longer support `UNKNOWN_ENUM_VALUE`. Instead, a `ValueError` will be raised if this property is assigned a value that it does not support.
* The properties `lifecycle_state`, `kind`, and `last_execution_status` in the `Rule` model in the Log Analytics service were fixed to no longer support `UNKNOWN_ENUM_VALUE`. Instead, a `ValueError` will be raised if these properties are assigned a value that they do not support.
* The properties `type` and `lifecycle_state` in the `Parameter` model in the Digital Assistant service were fixed to no longer support `UNKNOWN_ENUM_VALUE`. Instead, a `ValueError` will be raised if these properties are assigned a value that they do not support.
* The property `model_type` in the `AbstractField`, `ConnectionDetails`, `Filter`, `Operation`, and `Source` models in the Data Integration service was fixed to no longer support `UNKNOWN_ENUM_VALUE`. Instead, a `ValueError` will be raised if this property is assigned a value that it does not support.
* The property `baseline_ocpu_utilization` in the `LaunchInstanceShapeConfigDetails` model in the Compute service was fixed to no longer support `UNKNOWN_ENUM_VALUE`. Instead, a `ValueError` will be raised if this property is assigned a value that it does not support.
* The property `type` in the `AssetSource`, `AssetSourceCredentials`, and `AssetSourceSummary` models in the Cloud Migration service was fixed to no longer support `UNKNOWN_ENUM_VALUE`. Instead, a `ValueError` will be raised if this property is assigned a value that it does not support.
* The property `lifecycle_state` in the `AssetSource`, `AssetSourceConnection`, `AssetSourceSummary`, `DiscoverySchedule`, and `DiscoveryScheduleSummary` models in the Cloud Migration service was fixed to no longer support `UNKNOWN_ENUM_VALUE`. Instead, a `ValueError` will be raised if this property is assigned a value that it does not support.
* The property `connection_type` in the `AssetSourceConnection` model in the Cloud Migration Service was fixed to no longer support `UNKNOWN_ENUM_VALUE`. Instead, a `ValueError` will be raised if this property is assigned a value that it does not support.
 
====================
2.99.1 - 2023-04-25
====================

Added
-----
* Support for enabling mTLS authentication with Listener and for providing custom value for TLS port and Non-TLS Port during AVM Cluster Creation in Database service
* Support for usedDataStorageSizeInGbs property for autonomous database in the Database service
* Support for csiNumber organization in Tenant Manager Control Plane service
* Support for creating and updating an infrastructure with LACP support in Database service
* Support for changePrivateEndpointOutboundConnection operation in Integration Cloud service
* Support for Enable Process in Integration Cloud service
* Support for Disaster Recovery, DR enablement, switchover, and failover feature in Fusion Apps service
* Support for discovery and monitoring of External Exadata infrastructure in Database Management Service
 
====================
2.99.0 - 2023-04-18
====================

Added
-----
* Support for private endpoints in the Digital Assistant service
* Support for canceling backups in the Database service
* Support for improved labeling of key/value pairs in the Data Labeling service 
 
Breaking
--------
* Support for retries by default on operations of the Digital Assistant service
* The property `opc_retry_token` was removed from the models `configure_digital_assistant_parameters`, `rotate_channel_keys`, `start_channel`, `stop_channel` in the Digital Assistant service
- The property `lifetime_logical_clock` was removed from the models `Record`, `Dataset` and `Annotation` in the Digital Assistant service
- The property `digital_assistant_id` was renamed to `id` in the `list_digital_assistants` model in the Digital Assistant service
- The property `is_latest_skill_only` was renamed to `is_latest_version_only` in the `list_packages` method in the Digital Assistant service
- The property `skill_id` was renamed to `id` in the `list_skills` model in the Digital Assistant service
- The properties `authorization_endpoint_url` and `subject_claim` were made optional in the `AuthenticationProvider` model in the Digital Assistant service
 
====================
2.98.0 - 2023-04-11
====================

Added
-----
* Support for rotation of certificates on autonomous VM clusters on Exadata Cloud at Customer in the Database service
* Support for ACD and OKV wallet naming for autonomous databases and dedicated autonomous databases on Exadata Cloud at Customer in the Database service
* Support for Exadata cloud service application virtual IPs (VIPs) in the Database service
* Support for additional manageability features for large sensitive data models and masking policies in the Data Safe service
* Support for getting user profile details and assignments for databases and fleets in the Data Safe service
* Support for enabling ADDM spotlight for databases in the Operations Insights service  
 
Breaking
--------
* The property `additional_database_status` was removed from the models `AutonomousDatabase`, `AutonomousDatabaseSummary`, `AutonomousDataWarehouse`and `AutonomousDataWarehouseSummary` in the Database service  
 
====================
2.97.0 - 2023-04-04
====================

Added
-----
* Support for pre-emptible worker nodes in the Container Engine for Kubernetes service
* Support for larger data storage (now up to 128TB) in the MySQL Database service
* Support for HTTP health checks for HTTPS backend sets in the Load Balancer service  
 
Breaking
--------
* The property `backend_set_name` was made required in the `ForwardToBackendSet` model in the Load Balancer service
2.96.1 - 2023-03-28
====================

Added
-----
* Support for ACD and OKV wallet naming for autonomous databases and dedicated autonomous databases on Exadata Cloud at Customer in the Database service
* Support for validating the credentials of a connection in the DevOps service
* Support for GoldenGate Replicat performance profiles when creating a migration in the Database Migration service
* Support for connection diagnostics on registered databases in the Database Migration service
* Support for launching bare metal instances in an RDMA network in the Compute service
 
====================
2.96.0 - 2023-03-21
====================

Added
-----
* Support for backup automation integration with the Database Recovery service in the Database service
* Support for changing the disaster recovery configuration of an autonomous database in remote regions of its disaster recovery association in the Database service
* Support for creating a remote disaster recovery association clone of an autonomous database in the Database service
* Support for managed build stages to be configured to use custom shape build runners in the DevOps service
* Support for listing pre-built functions and creating functions from pre-built functions in the Functions service
* Support for connections types for database resources of type Amazon S3, HDFS, SQL Server, Java Messaging service, Mongo DB, Oracle NoSQL, and Snowflake in the GoldenGate service

Breaking
--------
* The constant value `MODEL_TYPE_LAKE_HOUSE_CONNECTION` was renamed to `MODEL_TYPE_LAKE_CONNECTION` in the Connection, ConnectionDetails, ConnectionSummary, CreateConnectionDetails and UpdateConnectionDetails models in the Data Integration Service
* The constant value `MODEL_TYPE_LAKE_HOUSE_DATA_ASSET` was renamed to `MODEL_TYPE_LAKE_DATA_ASSET` in the enum ModelTypeEnum in the DataAsset, CreateDataAssetDetails, DataAssetSummary, and UpdateDataAssetDetails models in the Data Integration Service
* Model `UpdateConnectionFromLakehouse` was renamed to `UpdateConnectionFromLake` in the Data Integration Service
* The constant values for `lifecycle_state` property of model `FunctionSummary` are removed in the Functions Service

====================
2.95.0 - 2023-03-14
====================

Added
-----
* Support for the Identity Domains service
* Support for long-term backups for autonomous databases on Exadata Cloud at Customer in the Database service
* Support for database OS patching in the Database service
* Support for managing enhanced clusters, cluster add-ons, and serverless virtual node pools in the Container Engine for Kubernetes service
* Support for templates and copy object requests in the Data Integration service
* Support for maintenance features in the GoldenGate service
* Support for AMD_MILAN_BM_GPU configuration type on instances in the Compute service
* Support for host storage metrics and network metrics as part of host capacity planning in the Operations Insights service
 
Breaking
--------
* `UNKNOWN_ENUM_VALUE` will be returned for unknown enum values, instead of raising `ValueError`, for property `protocol` in model `IdentityProvider` in the Identity Data Plane service
* `UNKNOWN_ENUM_VALUE` will be returned for unknown enum values, instead of raising `ValueError`, for property `lifecycle_state` in model `TemplateSummary` in the Identity Data Plane service
 
Security
--------
* The upper bound for `cryptography` dependency has changed to versions less than `40.0.0` to address security vulnerability CVE-2023-23931. For more discussion please see https://github.com/oracle/oci-python-sdk/issues/515
  
====================
2.94.0 - 2023-03-07
====================

Added
-----
* Support for creating and updating autonomous database long-term backup schedules in the Database service
* Support for creating, updating, and deleting autonomous database long-term backups in the Database service
* Support for model deployment resources to use customized container images containing runtime dependencies of ML models and custom web servers to handle inference requests in the Data Science service
* Support for using the compartmentIdInSubtree parameter when summarizing management agent counts in the Management Agent Cloud service
* Support for getting agent property details in the Management Agent Cloud service
* Support for filtering by gateway ID when listing agents in the Management Agent Cloud service
* Support for the Hebrew and Greek languages during AI language text translation in the AI Language service
* Support for auto-detection when analyzing text with pre-trained models in the AI Language service
* Support for specifying update operation constraints when updating an instance in the Compute Service
* Support for disaster recovery in the Content Management service
* Support for advanced autonomous databases insights in the Operations Insights service  
 
Breaking
--------
* Support for retries by default on operations of the Analytics Cloud service
* The value `ACTIVE` was removed from `LifecycleDetails` in the `OceInstanceSummary` and `OceInstance` model in the Content Management service 
 
====================
2.93.1 - 2023-02-28
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the eu-dcc-rating-1, eu-dcc-rating-2, eu-dcc-dublin-1, eu-dcc-dublin-2, and eu-dcc-milan-2 regions
* Support for on-demand bootstrap script execution in the Big Data Service
 
====================
2.93.0 - 2023-02-21
====================

Added
-----
* Support for async jobs in the AI Anomaly Detection service
* Support for specifying algorithm hints and windows sizes during model training in the AI Anomaly Detection service
* Support for specifying a sensitivity value during model detection in the AI Anomaly Detection service
* Support for discovery and monitoring of external Oracle database infrastructure components in the Database Management service
 
Breaking
--------
* The type for property `system_tags` was changed from a dict of string to another dict to a dict of a string to object for `project_summary`, `project`, `model_summary`, `model`, `data_asset_summary`, `data_asset`, `ai_private_endpoint_summary`, `ai_private_endpoint` models in the AI Anomaly Detection service
* Support for retries by default on operations of the AI Anomaly Detection service
 
====================
2.92.0 - 2023-02-14
====================

Added
-----
* Support for the Visual Builder Studio service
* Support for the Autonomous Recovery service
* Support for retries by default on operations of the Compute service
* Support for selecting specific database servers when creating autonomous VM clusters in the Database service
* Support for creating autonomous VMs during the creation of autonomous VM clusters in the Database service

Breaking
--------
* Support for retries by default on operations of the Compute service

====================
2.91.0 - 2023-02-07
====================

Added
-----
* Support for changing Data Guard role of a database instance within the Database service
* Support for listing autonomous container database versions in the Database service
* Support for specifying a database version when creating or updating an autonomous container database in the Database service
* Support for specifying an eCPU count when creating or updating autonomous shared databases in the Database service
* Support for Helm attestation and Helm arguments on deploy operations in the DevOps service
* Support for uploading master key wallets for deployments in the GoldenGate service
* Support for custom configurations in the Operations Insights service  
 
Breaking
--------
* Field `cpu_core_count` has been made optional in the models `AutonomousDatabaseSummary` and `AutonomousDatabase` in the Database service
 
====================
2.90.4 - 2023-01-31
====================

Added
-----
* Support for ECPU billing for autonomous databases and dedicated autonomous databases on Exadata Cloud at Customer in the Database service
* Support for providing a vault secret ID when creating or updating autonomous shared databases in the Database service
* Support for including ORDS and database transform URLs as autonomous database connections in the Database service
* Support for role-based access control on OpenSearch clusters in the Search service
* Support for managed shell stages on deployments in the DevOps service
* Support for memory encryption on confidential VMs in the Compute service
* Support for configuration items, and reporting ownership of configuration items, in the Application Performance Monitoring service

====================
2.90.3 - 2023-01-24
====================

Added
-----
* Support for the Cloud Migrations service
* Support for setting up custom private IPs while creating private endpoints in the Database service
* Support for machine learning pipelines in the Data Science service
* Support for personally identifiable information detection in the AI Language service  
 
====================
2.90.2 - 2023-01-17
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the us-chicago-1 region
* Support for cross-region replication in the File Storage service
* Support for setting up private DNS on ExaCS systems during provisioning in the Database service
* Support for elastic storage expansion on infrastructure resources for Exadata Cloud at Customer in the Database service
* Support for target versions during infrastructure patching on Cloud Exadata infrastructure in the Database service
* Support for creating model version sets in the model catalog in the Data Science service
* Support for associating a model with a model version set in the Data Science service
* Support for custom key/value annotations on documents in the Data Labeling service
* Support for configurable timeouts in the Service Mesh service  
 
====================
2.90.1 - 2023-01-10
====================

Security
--------
* Upgrade wheel version for applicable Python versions to fix security vulnerability as mentioned in https://github.com/oracle/oci-python-sdk/pull/502

====================
2.90.0 - 2022-12-13
====================

Added
-----
* Support for the Queue service
* Support for Intel X9 shapes when launching VM database systems in the Database service
* Support for enabling, disabling, and editing Database Management service connections on pluggable databases in the Database service
* Support for availability configurations and maintenance window schedules on synthetic monitors in the Application Performance Monitoring service
* Support for scheduling cascading deletes on a project in the DevOps service
* Support for cancelling a scheduled cascading delete on a project in the DevOps service
* Support for issue and action fields on job phases of validation and migration processes in the Database Migration service
* Support for cluster profiles in the Big Data service
* Support for egress-only services in the Service Mesh service
* Support for optional listeners and service discovery metadata on virtual deployments in the Service Mesh service
* Support for canceling work requests in the accepted state in the Service Mesh service
* Support for filtering work requests on associated resource id and operation status in the Service Mesh service
* Support for sorting while listing work requests, listing work request logs, and listing work request errors in the Service Mesh service
* Support for Oracle Managed Access integration in the Fusion Apps as a Service service
* Support for refresh scheduling in the Fusion Apps as a Service service
* Support for additional connections types on database resources in the GoldenGate service
* Support for retries by default on operations of the Fusion Apps as a Service service
* Support for retries by default on operations of the Database Migration service
* Support for retries by default on operations of the Service Mesh service    
 
Breaking
--------
* Support for default retries on operations of the Service Mesh service
* Support for default retries on operations of the Database Migration service
* Support for default retries on operations of the Fusion Apps as a Service service
* The property `service_instance_type` changed from optional to required in the model `AttachExistingInstanceDetails` in Fusion Apps as a Service service
* The property `instance_id` changed from optional to required in the model `AttachExistingInstanceDetails` in Fusion Apps as a Service service
* The property `details` changed from optional to required in the model `CreateNewInstanceDetails` in Fusion Apps as a Service service
* The property `name` changed from optional to required in the model `CreateOaxServiceInstanceDetails` in Fusion Apps as a Service service
* The property `adw_admin_pass` changed from optional to required in the model `FawAdminInfoDetails` in Fusion Apps as a Service service
* The property `notification_email` changed from optional to required in the model `FawAdminInfoDetails` in Fusion Apps as a Service service
* The type of property `rules` changed from a list of `AccessPolicyRule` to list of `AccessPolicyRuleDetails` for model `CreateAccessPolicyDetails` in the Service Mesh service
* The type of property `rules` changed from a list of `AccessPolicyRule` to list of `AccessPolicyRuleDetails` for model `UpdateAccessPolicyDetails` in the Service Mesh service
* The type of property `mtls` changed from `CreateIngressGatewayMutualTransportLayerSecurityDetails` to `IngressGatewayMutualTransportLayerSecurityDetails` for model `CreateIngressGatewayDetails` in the Service Mesh service
* The type of property `mtls` changed from `CreateIngressGatewayMutualTransportLayerSecurityDetails` to `IngressGatewayMutualTransportLayerSecurityDetails` for model `UpdateIngressGatewayDetails` in the Service Mesh service
* The type of property `mtls` changed from `CreateMutualTransportLayerSecurityDetails` to `VirtualServiceMutualTransportLayerSecurityDetails` for model `CreateVirtualServiceDetails` in the Service Mesh service
* The type of property `mtls` changed from `CreateMutualTransportLayerSecurityDetails` to `VirtualServiceMutualTransportLayerSecurityDetails` for model `UpdateVirtualServiceDetails` in the Service Mesh service
* The type of property `route_rules` changed from list of `IngressGatewayTrafficRouteRule` to list of `IngressGatewayTrafficRouteRuleDetails` for model `CreateIngressGatewayRouteTableDetails` in the Service Mesh service
* The type of property `route_rules` changed from list of `IngressGatewayTrafficRouteRule` to list of `IngressGatewayTrafficRouteRuleDetails` for model `UpdateIngressGatewayRouteTableDetails` in the Service Mesh service
* The type of property `route_rules` changed from list of `VirtualServiceTrafficRouteRule` to list of `VirtualServiceTrafficRouteRuleDetails` for model `CreateVirtualServiceRouteTableDetails` in the Service Mesh service
* The type of property `route_rules` changed from list of `VirtualServiceTrafficRouteRule` to list of `VirtualServiceTrafficRouteRuleDetails` for model `UpdateVirtualServiceRouteTableDetails` in the Service Mesh service
 
====================
2.89.0 - 2022-12-06
====================

Added
-----
* Support for the Container Instances service
* Support for the Document Understanding service
* Support for creating stacks from OCI DevOps service and Bitbucket Cloud/Server as source control management in the Resource Manager service
* Support for deployment stage level parameters in the DevOps service
* Support for PeopleSoft discovery in the Stack Monitoring service
* Support for Apache Tomcat discovery in the Stack Monitoring service
* Support for SQL Server discovery in the Stack Monitoring service
* Support for OpenId Connect in the API Gateway service
* Support for returning compartment ids when listing backups in the MySQL Database service
* Support for adding a load balancer endpoint to a DB system in the MySQL Database service
* Support for managed read replicas in the MySQL Database service
* Support for setting replication filters on channels in the MySQL Database service
* Support for replicating from a source configured without global transaction identifiers into a channel in the MySQL Database service
* Support for time zone and language preferences in the Announcements service
* Support for adding report schedules for activity auditing and alerts reports in the Data Safe service
* Support for bulk operations on alerts in the Data Safe service
* Support for Java server usage reporting in the Java Management service
* Support for Java library usage reporting in the Java Management service
* Support for cryptographic roadmap impact analysis in the Java Management service
* Support for Java Flight Recorder recordings in the Java Management service
* Support for post-installation steps in the Java Management service
* Support for restricting management of advanced functionality in the Java Management service
* Support for plugin improvements in the Java Management service
* Support for collecting diagnostics on deployments in the GoldenGate service
* Support for onboarding Exadata Public Cloud (ExaCS) targets to the Operations Insights service  
 
Breaking
--------
* Parameter `autonomous_database_id` of model `AutonomousDatabaseDetails` changed from optional to required in the Data Safe service
* Parameter `listener_port` of model `InstalledDatabaseDetails` changed from optional to required in the Data Safe service
* Parameter `service_name` of model `InstalledDatabaseDetails` changed from optional to required in the Data Safe service
* Parameter `compartment_id` of model `PatchAlertsDetails` changed from optional to required in the Data Safe service
 
====================
2.88.2 - 2022-11-22
====================

Added
-----
* Support for Resource Principals version 2.1 and 2.1.1
* Support for disabling Lazy Imports introduced in version `2.88.1` by setting the environment variable `OCI_PYTHON_SDK_LAZY_IMPORTS_DISABLED` to `True`
 
Changed
-------
* The upper bound for `cryptography` dependency has changed from `37.0.2` to versions less than `39.0.0`

====================
2.88.1 - 2022-11-15
====================

Added
-----
* Support for mTLS authentication with listeners during Autonomous VM Cluster creation on Exadata Cloud at Customer in the Database service
* Support for providing custom values for TLS and non-TLS ports during Autonomous VM Cluster creation on Exadata Cloud at Customer in the Database service
* Support for creating multiple Autonomous VM Clusters in the same Exadata infrastructure in the Database service
* Support for listing resources associated with a job in the Resource Manager service
* Support for listing resources associated with a stack in the Resource Manager service
* Support for listing outputs associated with a job in the Resource Manager service
* Support for the Oracle distribution of Apache Hadoop 2.0 in the Big Data service
 
Changed
-------
* Lazy Imports (based on `PEP 562 <https://peps.python.org/pep-0562/>`_) have been enabled by default for OCI modules when using a Python version 3.7 or up to reduce start up times.
 
====================
2.88.0 - 2022-11-08
====================

Added
-----
* Support for listing local and cross-region refreshable clones in the Database service
* Support for adding multiple cloud VM clusters in the Database service
* Support for creating rollback jobs in the Resource Manager service
* Support for edge nodes in the Big Data service
* Support for Single Client Access Name (SCAN) in the Data Flow service
* Support for additional filters when listing application dependencies in the Application Dependency Management service
* Support for additional properties when reading Vulnerability Audit resources in the Application Dependency Management service
* Support for optionally passing compartment IDs when creating Vulnerability Audit resources in the Application Dependency Management service  

Breaking
--------
* Property `certificate_id` changed from optional to required for model `PrivateServerConfigDetails` in the Resource Manager service

====================
2.87.0 - 2022-11-01
====================

Added
-----
* Support for cloning from a backup from the last available timestamp in the Database service
* Support for third-party scanning using Qualys in the Vulnerability Scanning service
* Support for customer-provided encryption keys in the Logging Analytics service
* Support for connections for database resources in the GoldenGate service  
 
Breaking
--------
* The properties `dataType`, `timeDataEnded`, `compartmentId` is made from required to optional from the `StorageWorkRequestSummary` model in Log Analytics service 
 
====================
2.86.0 - 2022-10-25
====================

Added
-----
* Support for the Disaster Recovery service
* Support for running code interactively with session applications using statements in the Data Flow service
* Support for language custom models and language translation in the AI Language service
 
Breaking
--------
* type `documents` is changed from `TextClassificationDocument` to `TextDocument` in `BatchDetectLanguageTextClassificationDetails` model in the AI Language service
* type `documents` is changed from `SentimentsDocument` to `TextDocument` in `BatchDetectLanguageSentimentsDetails` model in the AI Language service
* type `documents` is changed from `KeyPhraseDocument` to `TextDocument` in `BatchDetectLanguageKeyPhrasesDetails` model in the AI Language service
* type `documents` is changed from `EntityDocument` to `TextDocument` in `BatchDetectLanguageEntitiesDetails` model in the AI Language service
 
====================
2.85.0 - 2022-10-04
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the eu-dcc-milan-1 region
* Support for target host identification and SOCKS support on dynamic port forwarding sessions in the Bastion service
* Support for viewing top processes running at a particular point of time in the Operations Insights service
* Support for filtering top processes by a single process to view that process's trend over time in the Operations Insights service
* Support for creating Enterprise Manager-based Windows host targets in the Operations Insights service
* Support for creating Management Agent Cloud-based Windows and Solaris host targets in the Operations Insights service

Breaking
--------
* Parameter `target_resource_port` is removed from models `TargetResourceDetails` and `CreateSessionTargetResourceDetails`

====================
2.84.0 - 2022-09-27
====================

Added
-----
* Support for search capabilities for monitored resources in the Stack Monitoring service
* Support for deleting monitored resources with their members in the Stack Monitoring service
* Support for creating host-type monitored resources in the Stack Monitoring service
* Support for associating external resources during creation of monitored resources in the Stack Monitoring service
* Support for uploading bulk data in the NoSQL Database Cloud service
* Support for examining query execution plans in the NoSQL Database Cloud service
* Support for starting and stopping clusters in the Big Data service
* Support for additional compute shapes in the Big Data service
* Support for backwards pagination in the Search service
* Support for elastic compute for Exadata Cloud at Customer in the Database service  
 
Breaking
--------
* Support for default retries on operations of the NoSQL Database Cloud service
 
====================
2.83.0 - 2022-09-20
====================

Added
-----
* Support for the Cloud Bridge service
* Support for the Cloud Migrations service
* Support for display banners, trails, and sizes in the GoldenGate service
* Support for generic REST data assets, flattening of data in Data Flow, and runtime information on pipelines in the Data Integration service
* Support for expanded search functionality in the Threat Intelligence service
* Support for ingest-time rules and specifying logsets and query strings during recalls in the Logging Analytics service
* Support for repository mirroring from Visual Builder Studio in the DevOps service
* Support for running a managed build stage with the source code hosted in a Visual Builder Studio repository in the DevOps service
* Support for triggering a build run based on an event in a Visual Builder Studio repository in the DevOps service
* Support for additional parameters during cost management scheduling in the Usage service

Breaking
--------
* Support for retries by default on operations of the GoldenGate service
* Support for retries by default on operations of the Threat Intelligence service
* The property `threat_types` is change from an Array of `model.ThreatType` to an Array of `string` in the IndicatorSummary model in the Threat Intelligence service
* The property `deploy_stage_id` was made a required parameter in `CreateSingleDeployStageDeploymentDetails` and `CreateSingleDeployStageRedeploymentDetails` model in the DevOps service
* The property `PreviousDeploymentId` was made a required parameter in the `CreateDeployPipelineRedeploymentDetails` model in the DevOps service

====================
2.82.0 - 2022-09-13
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the eu-madrid-1 region
* Support for exporting and importing larger model artifacts in the model catalog in the Data Science service
* Support for Request Based Authorization in the API Gateway service
* Support for Dynamic Authentication in the API Gateway service
* Support for Dynamic Routing Backend in the API Gateway service
 
Breaking
--------
* Support for retries by default on some operations of the Data Science service
 
====================
2.81.0 - 2022-09-06
====================

Added
-----
* Support for generic REST, OCI Streaming service, and Lake House connectors in the Data Connectivity Management service
* Support for connecting to the Data Catalog service in the Data Connectivity Management service
* Support for Kerberos and SSL for HDFS operations in the Data Connectivity Management service
* Support for excel-formatted data and default columns in the Data Connectivity Management service
* Support for reporting connector usage in the Data Connectivity Management service
* Support for preferred credentials for performing privileged operations in the Database Management service
* Support for passing a content encoding when posting metrics in the Monitoring service  
 
Breaking
--------
* Support for retries by default on some operations of the Data Connectivity Management service
* Model `ConnectionValidationSummaryCollection` removed from the Data Connectivity Management service
* Operations `delete_connection_validation` and `list_connection_validations` removed from the `DataConnectivityManagementClient` of the Data Connectivity Management service
* Parameter `resource_id` renamed to `registry_id` in `list_work_requests` operation from the `DataConnectivityManagementClient` of the Data Connectivity Management service
 
====================
2.80.1 - 2022-08-30
====================

Added
-----
* Support for opting out of guest VM event collection, health metrics, diagnostics logs, and traces in the Database service
* Support for in-place upgrades for software-defined data centers in the VMWare Solution service
* Support for single-client access name protocol as a data source for private access channels in the Analytics Cloud service
* Support for network security groups, egress control on public datasources, and GitHub access in the Analytics Cloud service
* Support for performance-based autotuning of block and boot volumes in the Block Storage service

====================
2.80.0 - 2022-08-23
====================

Added
-----
* Support for the Enterprise Manager Warehouse service
* Support for additional configuration variables in the MySQL Database service
* Support for file filters in the DevOps service
* Support for support rewards redemption summaries in the Usage service
* Support for the parent tenancy of an organization to view child tenancy categories, recommendations, and resource actions in the Optimizer service
* Support for choosing prior versions during infrastructure maintenance on Exadata Cloud at Customer in the Database service

Breaking
--------
* `EmDataLakeClient` was renamed to `EmWarehouseClient` in the Enterprise Manager Warehouse service
* `EmDataLakeClientCompositeOperations` was renamed to `EmWarehouseClientCompositeOperations` in the Enterprise Manager Warehouse service

====================
2.79.0 - 2022-08-16
====================

Added
-----
* Support for Logging Analytics as a streaming source target in the Service Connector Hub service
* Support for data sources for logging query registration in the Cloud Guard service
* Support for custom detector rules on insight detector recipes in the Cloud Guard service
* Support for fetching data source events and problem entities in the Cloud Guard service
* Support for E3, E4, Standard3, and Optimized3 flexible compute shapes on notebooks, model deployment, and jobs in the Data Science service
* Support for streaming application logs to the Logging service in the Data Flow service
 
Breaking
--------
* Support for retries by default on operations of the Dataflow service
 
====================
2.78.0 - 2022-08-09
====================

Added
-----
* Support for single-host software-defined data centers in the VMWare Solution service
* Support for Java download and installation in the Java Management service
* Support for lifecycle management for Windows in the Java Management service
* Support for installation scripts in the Java Management service
* Support for unlimited-installation keys in the Java Management service
* Support for configuring automatic usage tracking in the Java Management service
* Support for STANDARDX and ENTERPRISEX instance types in Integration service
* Support for additional languages and multimedia formats in transcription jobs in the AI Speech service
* Support for maintenance run history for Exadata Cloud at Customer in the Database service
* Support for Optimizer statistics monitoring and management on various database administration operations in the Database Management service
* Support for OCI Compute instances in the Operations Insights service
* Support for moving resources in the Console Dashboard service
* Support for round-robin alerting in the Application Performance Monitoring service
* Support for aggregated network data of synthetic monitors in the Application Performance Monitoring service
* Support for etags on operations in the Load Balancing service

Breaking
--------
* The property `inventory_log` in create_fleet_details model was made a required parameter in Operations Insights service

====================
2.77.0 - 2022-08-02
====================

Added
-----
* Support for OpenSearch in the Search service
* Support for child tables in the NoSQL Database Cloud service
* Support for private repositories in the DevOps service
 
Breaking
--------
* Support for retries by default on operations of the Quotas service
 
====================
2.76.0 - 2022-07-27
====================

Added
-----
* Support for the Fusion Apps as a Service service
* Support for the Digital Media service
* Support for accessing all Terraform providers from Hashicorp Registry, as well as bringing your own providers, in the Resource Manager service
* Support for runtime configurations in notebook sessions in the Data Science service
* Support for compartmentIdInSubtree and accessLevel filters when listing management agents in the Management Agent Cloud service
* Support for filtering by type when listing work requests in the Management Agent Cloud service
* Support for filtering by agent id when listing management agent plugins in the Management Agent Cloud service
* Support for specifying size preference when requesting a data transfer appliance in the Data Transfer service
* Support for encryption of boot and block volumes associated with a cluster using customer-specified KMS keys in the Big Data service
* Support for the VM.Standard.E4.Flex shape for Cloud SQL (CSQL) nodes in the Big Data service
* Support for listing block and boot volumes, as well as block and boot volume replicas, within a volume group in the Block Volume service
* Support for dedicated autonomous databases in the Operator Access Control service
* Support for viewing automatic workload repository (AWR) data for databases added to AWRHub in the Operations Insights service
* Support for ports, protocols, roles, and SSL secrets when enabling or modifying database management in the Database service
* Support for monthly security maintenance runs in the Database service
* Support for monthly infrastructure patching for Exadata Cloud at Customer resources in the Database service
 
Breaking
--------
* `DataMaskingActivityClient`,`FusionEnvironmentClient`, `FusionEnvironmentFamilyClient`, `RefreshActivityClient`,`ScheduledActivityClient`, and `ServiceAttachmentClient` clients were merged into a single client `FusionApplicationsClient` for the Fusion Apps as a Service service
* Properties `addressee`, `address1`, `cityOrLocality`, `stateOrRegion`, `zipcode`, `country` are changed from optional to required for `ShippingAddress` model in Data Transfer Service
* Parameter `compartment_id` changed from required to optional in the `list_volumes` operation in `BlockstorageClient` in the Block Storage service
* Parameters `availability_domain` and `compartment_id` changed from required to optional in operations `list_boot_volumes`, `list_boot_volume_replicas`, `list_block_volume_replicas` in `BlockstorageClient` in the Block Storage service
 
====================
2.75.1 - 2022-07-19
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the mx-queretaro-1 region
* Support for the Process Automation service
* Support for the Managed Access service
* Support for extending maintenance reboot due dates on virtual machines in the Compute service
* Support for ingress routing tables on NAT gateways and internet gateways in the Networking service
* Support for container database and pluggable database discovery in the Stack Monitoring service
* Support for displaying rack serial numbers for Exadata infrastructure resources in the Database service
* Support for grace periods for wallet rotation on autonomous databases in the Database service
* Support for hosting models on flexible compute shapes with customizable OCPUs and memory in the Data Science service
 
Changed
-------
* The upper bound for `pyOpenSSL` dependency has changed from `19.1.0` to `22.0.0`
* The upper bound for `cryptography` dependency has changed from `3.4.7` to `37.0.2`
 
====================
2.75.0 - 2022-07-12
====================

Added
-----
* Support for DBCS databases in the Operations Insights service
* Support for point-in-time recovery for non-highly-available database systems in the MySQL Database service
* Support for triggering reboot migration on instances with pending maintenance in the Compute service
* Support for native pod networking in the Container Engine for Kubernetes service
* Support for creating Data Guard associations with new database systems in the Database service
 
Breaking
--------
* Parameter `host_type` in operation `list_host_insights` in the Operations Insights service has strict value checking for allowed values. `ValueError` is raised if an invalid value is provided.
* Parameter `preserve_data_volumes` is removed from operation `terminate_instance` in the Compute service.
 
====================
2.74.0 - 2022-07-05
====================

Added
-----
* Support for backup policies returned as part of the database system list operation in the MySQL Database service
 
Breaking
--------
* Support for retries by default on some operations of the Bastion service
 
====================
2.73.0 - 2022-06-27
====================

Added
-----
* Support for the Network Monitoring service
* Support for specifying application scan settings when creating or updating host scan recipes in the Vulnerability Scanning service
* Support for moving data into an autonomous data warehouse in the Operations Insights service
* Support for shared infrastructure autonomous database character sets in the Database service
* Support for data collection logging events on Exadata instances in the Database service
* Support for specifying boot volume VPUs when launching instances from images in the Compute service
* Support for safe-deleting nodes in the Container Engine for Kubernetes service

Breaking
--------
* Support for retries by default on operations of the Logging Analytics service

====================
2.72.0 - 2022-06-21
====================

Added
-----
* Support for the Network Firewall service
* Support for smaller and larger HeatWave cluster nodes in the MySQL Database service
* Support for CSV file type datasets for text labeling and JSONL in the Data Labeling service
* Support for diagnostics in the Database Management service
 
Breaking
--------
* Support for retries by default on operations of the Network Firewall service
* Support for retries by default on the createAnnotation operation of the Data Labeling service
 
====================
2.71.0 - 2022-06-14
====================

Added
-----
* Support for the Web Application Acceleration (WAA) service
* Support for the Governance Rules service
* Support for the OneSubscription service
* Support for resource locking in the Identity service
* Support for quota resource locking in the Limits service
* Support for returning the backup with the requested changes in the MySQL Database service
* Support for time zone in Cloud Autonomous VM (CAVM) clusters in the Database service
* Support for configuration options in the Application Performance Monitoring service
* Support for MySQL connections in the Database Tools service

Breaking
--------
* The models `DatabaseToolsAllowedNetworkSources`, `DatabaseToolsVirtualSource`, and `ServiceCapability` are removed from the Database Tools service
* The property `SecretId` is made a required property in the `DatabaseToolsUserPasswordSecretIdDetails` model in the Database Tools service
* Response type for operation `update_backup` is changed to `oci.mysql.models.Backup` from `None` in the `DbBackupsClient` of the MySQL service

====================
2.70.1 - 2022-06-07
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the eu-paris-1 region
* Support for private endpoints in Resource Manager service
* Support downloading generated Terraform plan output in JSON or binary format in Resource Manager service
* Support for querying OPSI Data Objects in the Operations Insights service

Changed
-------
* Network security groups (NSGs) are now optional for autonomous databases on private endpoints in the Database service

====================
2.70.0 - 2022-05-31
====================

Added
-----
* Support for in-depth monitoring, diagnostics capabilities, and advanced management functionality for on-premise Oracle databases in the Database Management service
* Support for using Oracle Cloud Agent to perform iSCSI login and logout for non-multipath-enabled iSCSI attachments in the Container Engine for Kubernetes service
* Support for Fault Domain placement in the Container Engine for Kubernetes service
* Support for worker node images in the Container Engine for Kubernetes service
* Support for flexible shapes using the driverShapeConfig and executorShapeConfig properties in the Data Flow service

Breaking
--------
* Support for retries by default on operations in the Application Dependency Management service

====================
2.69.0 - 2022-05-24
====================

Added
-----
* Support for the License Manager service
* Support for usage plans in the API Gateway service
* Support for packaged skill and instance metadata management, role-based access options on instance creation, and assigned ownership in the Digital Assistant service
* Support for compute capacity reservations in the VMWare Solution service
* Support for Oracle Linux 8 application streams in the OS Management service
 
Breaking
--------
* Support for retries by default on operations in the API Gateway service
* The property `specification` is now a required parameter for the deployment model in the API Gateway service
* The property `specification` is now a required parameter for the create_deployment_details model in the API Gateway service
 
Changed
-------
* The vendored dependency `requests` was upgraded from version `2.21.0` to `2.27.1`
* The vendored dependency `urllib3` was upgraded from version `1.24.1` to `1.26.9`
* The vendored dependency `chardet` was upgraded from version `3.0.4` to `4.0.0`
* The vendored dependency `idna` was upgraded from version `2.8` to `2.10`
* The vendored dependency `six` was upgraded from version `1.12.0` to `1.16.0`
 
====================
2.68.0 - 2022-05-17
====================

Added
-----
* Support for information requests in the Operator Access Control service
* Support for Helm charts and repositories on deployments in the DevOps service
* Support for Application Dependency Management service scan results on builds in the DevOps service
* Support for build resources to use Bitbucket Cloud repositories for source code in the DevOps service
* Support for character set selection on autonomous dedicated databases in the Database service
* Support for listing autonomous dedicated database supported character sets in the Database service
* Support for AMD E4 flex shapes on virtual machine database systems in the Database service
* Support for terraform and improvements for cross-region ADGs in the Database service

Breaking
--------
* Support for retries by default on GET and LIST operations in the Visual Builder service

====================
2.67.0 - 2022-05-10
====================

Added
-----
* Support for getting usage information for autonomous databases and Cloud at Customer autonomous databases in the Database service
* Support for the "standby" lifecycle state on autonomous databases in the Database service
* Support for BIP connections and dataflow operators in the Data Integration service
 
Breaking
--------
* The type of parameter `default_connection` was changed from `CreateConnectionFromBICC` to `CreateConnectionDetails` in the create_data_asset_from_fusion_app model in the Data Integration service
* The type of parameter `default_connection` was changed from `ConnectionFromBICCDetails` to `ConnectionDetails` in the data_asset_from_fusion_app model in the Data Integration service
* The type of parameter `default_connection` was changed from `ConnectionSummaryFromBICC` to `ConnectionSummary` in the data_asset_summary_from_fusion_app model in the Data Integration service
* The type of parameter `output_ports` was changed from a list of oci.data_integration.models.OutputPort to oci.data_integration.models.TypedObject in the aggregator model in the Data Integration service
* Support for retries by default on WAF Edge Policy GET / LIST operations in the Web Application Acceleration and Security service
* Support for retries by default on some operations in the Stack Monitoring service
* Support for retries by default on some resource discovery and monitoring operations in the Application Management service
* Support for retries by default on some operations in the MySQL Database service
 
====================
2.66.0 - 2022-05-03
====================

Added
-----
* Support for the Application Dependency Management service
* Support for platform configuration options on some bare metal shapes in the Compute service
* Support for shielded instances for BM.Standard.E4.128 and BM.Standard3.64 shapes in the Compute service
* Support for E4 dense VMs on launch and update instance operations in the Compute service
* Support for reboot migration on DenseIO shapes in the Compute service
* Support for an increased database name maximum length, from 14 to 30 characters, in the Database service
* Support for provisioned concurrency in the Functions service
 
Breaking
--------
* Support for retries by default on operations in the Vault service
* Support for retries by default on operations in the DNS service
* Support for retries by default on operations in the Content Management service
* Support for retries by default on operations in the Console Dashboard service
* Support for retries by default on Web Application Firewall operations in the Web Application Acceleration and Security service
* Support for retries by default on operations in the Data Science service

====================
2.65.0 - 2022-04-26
====================

Added
-----
* Support for the Service Mesh service
* Support for security zones in the Cloud Guard service
* Support for virtual test access points (VTAPs) in the Networking service
* Support for monitoring as a source in the Service Connector Hub service
* Support for creating budgets that target subscriptions and child tenancies in the Budgets service
* Support for listing shapes and specifying a shape during creation of a node in the Roving Edge Infrastructure service
* Support for bringing your own key in the Roving Edge Infrastructure service
* Support for enabling inspection of HTTP request bodies in the Web Application Acceleration and Security
* Support for cost management schedules in the Usage service
* Support for TCPS on external containers as well as non-container and pluggable databases in the Database service
* Support for autoscaling on Open Data Hub (ODH) clusters in the Big Data service
* Support for creating Open Data Hub (ODH) 0.9 clusters in the Big Data service
* Support for Open Data Hub (ODH) patch management in the Big Data service
* Support for customizable Kerberos realm names in the Big Data service
* Support for dedicated vantage points in the Application Performance Monitoring service
* Support for reactivating child tenancies in the Organizations service
* Support for punctuation and the SRT transcription format in the AI Speech service

Breaking
--------
* Support for default retries on some operations in the Networking service
* Support for default retries on all operations in the Data Safe service
* Support for default retries on some additional operations in the Application Performance Monitoring service
* Property `risk_score` is removed from model `Sighting` in the Cloud Guard service
* `subscription_id` is a required parameter for operation `list_subscription_mappings` in the subscription client in Tenant Manager control plane service

====================
2.64.0 - 2022-04-19
====================

Added
-----
* Support for the Stack Monitoring service
* Support for stack monitoring on external databases in the Database service
* Support for upgrading VM database systems in place in the Database service
* Support for viewing supported VMWare software versions when listing host shapes in the VMWare Solution service
* Support for choosing compute shapes when creating SDDCs and ESXi hosts in the VMWare Solution service
* Support for work requests on delete operations in the Vulnerability Scanning service
* Support for additional scan metadata in reports, including CVE descriptions, in the Vulnerability Scanning service
* Support for redemption codes in the Usage service

Breaking
--------
* Param `type` in model `DiscoveryDetails` assumes the value of `UNKNOWN_ENUM_VALUE` if it is assigned a value that is not of the allowed_values. It will not raise a `ValueError`.

====================
2.63.0 - 2022-04-12
====================

Added
-----
* Support for bringing your own IPv6 addresses in the Networking service
* Support for specifying database edition and maximum CPU core count when creating or updating an autonomous database in the Database service
* Support for enabling and disabling data collection options when creating or updating Exadata Cloud at Customer VM clusters in the Database service
 
Breaking
--------
* Support for retries by default on operations in the Identity service
* Support for retries by default on operations in the Operations Insights service
 
====================
2.62.1 - 2022-04-05
====================

Added
-----
* Fixed the lifecycle state values for target databases in the Data Safe service
* Support for content length and content type response headers when downloading PDFs in the Account Management service
* Support for creating Enterprise Manager-based zLinux host targets, creating alarms, and viewing top process analytics in the Operations Insights service
* Support for diagnostic reboots on VM instances in the Compute service

====================
2.62.0 - 2022-03-29
====================

Added
-----
* Support for returning the number of network ports as part of listing shapes in the Compute service
* Support for Java runtime removal and custom logs in the Java Management service
* Support for new parameters for BGP admin state and enabling/disabling BFD in the Networking service
* Support for private OKE clusters and blue-green deployments in the DevOps service
* Support for international customers to consume and launch third-party paid listings in the Marketplace service
* Support for additional fields on entities, attributes, and folders in the Data Catalog service
 
Breaking
--------
* Support for retries by default on operations in the Marketplace service
 
====================
2.61.0 - 2022-03-22
====================

Added
-----
* Support for getting the storage utilization of a deployment on deployment list and get operations in the GoldenGate service
* Support for virtual machines, bare metal machines, and Exadata databases with private endpoints in the Operations Insights service
* Support for setting deletion policies on database systems in the MySQL Database service
 
Breaking
--------
* Support for retries by default on operations in the Data Labeling service (data plane and control plane)
 
====================
2.60.1 - 2022-03-15
====================

Added
-----
* Support for Ubuntu platforms and unlimited installation keys in the Management Agent Cloud service
* Support for shielded instances in the VMWare Solution service
* Support for application resources in the Data Integration service
* Support for multi-AVM on Exadata Cloud at Customer infrastructure in the Database service
* Support for heterogeneous (VM and AVM) clusters on Exadata Cloud at Customer infrastructure in the Database service
* Support for custom maintenance schedules for AVM clusters on Exadata Cloud at Customer infrastructure in the Database service
* Support for listing vulnerabilities, vulnerability-impacted containers, and vulnerability-impacted hosts in the Vulnerability Scanning service
* Support for specifying an image count when creating or updating container scan recipes in the Vulnerability Scanning service

====================
2.60.0 - 2022-03-08
====================

Added
-----
* Support for the Sales Accelerator license option in the Content Management service
* Support for VCN hostname cluster endpoints in the Container Engine for Kubernetes service
* Support for optionally specifying an admin username and password when creating a database system during a restore operation in the MySQL Database service
* Support for automatic tablespace creation on non-autonomous and autonomous database dedicated targets in the Database Migration service
* Support for reporting excluded objects based on static exclusion rules and dynamic exclusion settings in the Database Migration service
* Support for removing, listing, and adding database objects reported by the Cloud Premigration Advisor Tool (CPAT) in the Database Migration service
* Support for migrating Oracle databases from the AWS RDS service to OCI as autonomous databases, using the AWS S3 service and DBLINK for data transfer, in the Database Migration service
* Support for querying additional fields of a resource using return clauses in the Search service
* Support for clusters and station clusters in the Roving Edge Infrastructure service
* Support for creating database systems and database homes using customer-managed keys in the Database service
 
Breaking
--------
* Support for retries enabled by default on operations in the Container Engine for Kubernetes service
* Support for retries enabled by default on operations in the Resource Manager service
* Support for retries enabled by default on operations in the Search service
 
====================
2.59.0 - 2022-03-01
====================

Added
-----
* Support for DRG route distribution statements to be specified with a new match type 'MATCH_ALL' for matching criteria in the Networking service
* Support for VCN route types on DRG attachments for deciding whether to import VCN CIDRs or subnet CIDRs into route rules in the Networking service
* Support for CPS offline reports in the Database service
* Support for infrastructure patching v2 features in the Database service
* Support for auto-scaling the storage of an autonomous database, as well as shrinking an autonomous database, in the Database service
* Support for managed egress via a default networking option on jobs and notebooks in the Data Science service
* Support for more types of saved search enums in the Management Dashboard service

Breaking
--------
* Support for retries enabled by default on some operations in the AI Vision service

====================
2.58.0 - 2022-02-22
====================

Added
-----
* Support for the Data Connectivity Management service
* Support for the AI Speech service
* Support for disabling crash recovery in the MySQL Database service
* Support for detector recipes of type "threat", new detector rule of type "rogue user", and sightings operations in the Cloud Guard service
* Support for more VM shape configurations when listing shapes in the Compute service
* Support for customer-managed encryption keys in the Analytics Cloud service
* Support for FastConnect device information in the Networking service
 
Breaking
--------
* Support for retries enabled by default on all operations in the Application Performance Monitoring control plane service

====================
2.57.0 - 2022-02-15
====================

Added
------
* Support for the AI Vision service
* Support for the Threat Intelligence service
* Support for creation of NoSQL database tables with on-demand throughput capacity in the NoSQL Database Cloud service
* Support for tagging features in the Oracle Container Engine for Kubernetes (OKE) service
* Support for trace snapshots in the Application Performance Monitoring service
* Support for auditing and alerts in the Data Safe service
* Support for data discovery and data masking in the Data Safe service
* Support for customized subscriptions and delivery of announcements by email and SMS in the Announcements service

Breaking
--------
* The API `query_old` was removed from `query_client` in the Application Performance Monitoring service
 
====================
2.56.0 - 2022-02-08
====================

Added
-----
* Support for managing tablespaces in the Database Management service
* Support for upgrading and managing payment for subscriptions in the Account Management service
* Support for listing fast launch job configurations in the Data Science service

Breaking changes
-----
* Support for retries enabled by default on all operations in the Application Performance Monitoring service
* The type for the `bill_to_address` parameter was changed from `Address` to `BillToAddress` in the invoice model of the Account Management service
* `payment_method` was made a required property of the `payment_detail` model of the Account Management service

====================
2.55.1 - 2022-02-01
====================

Added
------
* Support for calling Oracle Cloud Infrastructure services in the ap-dcc-canberra-1 region
* Support for the Console Dashboard service
* Support for capacity reservation in the Container Engine for Kubernetes service
* Support for tagging in the Container Engine for Kubernetes service
* Support for fetching listings by image OCID in the Marketplace service
* Support for underscores and hyphens in project resource names in the DevOps service
* Support for cross-region cloning in the Database service

====================
2.55.0 - 2022-01-25
====================

Added
-----
* Support for OneSubscription services
* Support for specifying if a run or application is streaming or batch in the Data Flow service
* Support for updating the Instance Configuration of an Instance Pool within a Cluster Network in the Compute Management service
* Updated documentation for Cross Region ADG feature for Autonomous Database in the Database service
 
Breaking
--------
* Support for retries enabled by default on all operations in the Object Storage service
====================
2.54.1 - 2022-01-18
====================

Added
------
* Support for calling Oracle Cloud Infrastructure services in the me-dcc-muscat-1 region
* Support for the Visual Builder service
* Support for cross-region replication of volume groups in the Block Storage service
* Support for boot volume encryption in the Container Engine for Kubernetes service
* Support for adding metadata to records when creating and updating records in the Data Labeling service
* Support for global export formats in snapshot datasets in the Data Labeling service
* Support for adding labeling instructions to datasets in the Data Labeling service
* Support for updating autonomous dataguard associations for autonomous container databases in the Database service
* Support for setting up automatic failover when creating autonomous container databases in the Database service
* Support for setting the RECO storage size when updating a database system in the Database service
* Support for reconnecting refreshable clones to source for autonomous databases on shared infrastructure in the Database service
* Support for checking if an autonomous database on shared infrastructure can be reconnected to source, in the Database service

====================
2.54.0 - 2022-01-11
====================

Added
------
* Support for calling Oracle Cloud Infrastructure services in the af-johannesburg-1 region
* Support for multiple protocols on the same listener in the Network Load Balancing service
* IPv6 support in the Network Load Balancing service
* Support for creating Enterprise Manager-based Solaris and SunOS host targets in the Operations Insights service
* Support for choosing Data Guard type (Active Data Guard or regular) on databases in the Database service
* Support for allowing control characters in responses as requested in https://github.com/oracle/oci-python-sdk/issues/404. Please see the github issue for more details
 
Fixed
-----
* The root cause of the issue causing data corruption as mentioned in https://github.com/oracle/oci-python-sdk/issues/410 has been fixed. Please see the github issue for more details
 
Breaking
--------
* Support for retries enabled by default on all operations in the Java Management service

====================
2.53.1 - 2021-12-21
====================

Fixed
-----
* Fixes the potential data corruption issue as described in https://github.com/oracle/oci-python-sdk/issues/410. Customers using FIPS compliant openssl versions are advised to enable FIPS with the ways described in https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/fips-libraries.html.

====================
2.53.0 - 2021-12-14
====================

Added
-----
* Support for node replacement in the VMWare Solution service
* Support for ingestion of SQL stats metrics in the Operations Insights service
* Support for AWR hub integration in the Operations Insights service
* Support for automatically generating logical entities from filename patterns and relationships between business terms across glossaries in the Data Catalog service
* Support for automatic start/stop at scheduled times in the Database service
* Support for cloud VM cluster resources on autonomous dedicated databases in the Database service
* Support for external Hive metastores in the Big Data service
* Support for batch detection/inference in the AI Language service
* Support for dimensions on monitoring targets in the Service Connector Hub service
* Support for invoice operations in the Account Management service
* Support for custom CA trust stores in the API Gateway service
* Support for generating scoped database tokens in the Identity service
* Support for database passwords for users, for logging into database accounts, in the Identity service

Fixed
-----
* Fixed an issue where multipart upload operations to Object Storage service throws SSLError on Oracle Linux instances

Breaking
--------
* Support for retries enabled by default on some operations in the Data Catalog service
* Support for retries enabled by default on all operations in the Ocvp service

====================
2.52.1 - 2021-12-07
====================

Added
-----
* Support for the Application Management service
* Support for getting the inventory of JMS resources and listing Java runtime usage in a specified host in the Java Management service
* Support for categories, entity topology, and verifying scheduled tasks in the Logging Analytics service
* Support for RAC databases in the GoldenGate service
* Support for querying additional fields of a resource using return clauses in the Search service
* Support for key versions and key version OCIDs in the Key Management service

====================
2.52.0 - 2021-11-30
====================

Added
-----
* Support for SQL Tuning Advisor in the Database Management service
* Support for listing users and getting user details in the Database Management service
* Support for autonomous databases in the Database Management service
* Support for enabling and disabling Database Management features on autonomous databases in the Database service
* Support for the Solaris platform in the Management Agent Cloud service
* Support for cross-compartment operations in the Operations Insights service
* Support for listing deployment backups in the GoldenGate service
* Support for standard tags in the Identity service
* Support for viewing problems for deleted targets in the Cloud Guard service
* Support for choosing a platform version while creating a platform instance in the Blockchain Platform service
* Support for custom IPSec connection tunnel internet key exchange phase 1 and phase 2 encryption algorithms in the Networking service
* Support for pagination when listing work requests corresponding to an APM domain in the Application Performance Monitoring service
* Support for the "deleted" lifecycle state on APM domains in the Application Performance Monitoring service
* Support for calling Oracle Cloud Infrastructure services in the eu-milan-1 and me-abudhabi-1 regions

Breaking
--------
* Support for retries enabled by default in all operations of the DevOps, Build, and Source Code Management services

====================
2.51.0 - 2021-11-17
====================

Added
-----
* Support for getting subnet topology in the Networking service
* Support for encrypted FastConnect resources in the Networking service
* Support for performance and high availability, as well as recommendation metrics, in the Optimizer service
* Support for optional TDE wallet passwords in the Database service
* Support for Object Storage service integration in the Big Data service

Breaking
--------
* Support for circuit breakers enabled by default in all services except Streaming and Compute
* Support for retries enabled by default in all operations of the Functions and Roving Edge services, and in some operations of the Streaming service.

====================
2.50.0 - 2021-11-09
====================

Added
-----
* Support for drill down metadata in the Management Dashboard service
* Support for operator access control on dedicated autonomous databases in the Operator Access Control service

Breaking
--------
* Property `resource_type` and `is_enforced_always` from model `CreateOperatorControlAssignmentDetails` changed from optional to required in the Operator Access Control service
* Property `operator_control_name`, `approver_groups_list` and `is_fully_pre_approved` from model `UpdateOperatorControlDetails` changed from optional to required in the Operator Access Control service
* Property `is_enforced_always` from model `UpdateOperatorControlAssignmentDetails` changed from optional to required in the Operator Access Control service
* Property `approver_groups_list` and `is_fully_pre_approved` from model `CreateOperatorControlDetails` changed from optional to required in the Operator Access Control service
* Data type for response of operation `create_operator_control_assignment` changed to `oci.operator_access_control.models.OperatorControlAssignment` in the Operator Access Control service
====================
2.49.1 - 2021-11-02
====================

Added
-----
* Support for the Database Tools service
* Support for scan listener port TCP and TCP SSL on cloud VM clusters in the Database service
* Support for domains in the Identity service
* Support for redeemable users and support rewards in the Usage service
* Support for calling Oracle Cloud Infrastructure services in the ap-singapore-1 and eu-marseille-1 regions
* Support for second level domain fallback via environment variable.

Changed
-------
* Endpoint for Identity service changed to include `.oci` subdomain

====================
2.49.0 - 2021-10-26
====================

Added
-----
* Support for the Source Code Management service
* Support for the Build service
* Support for the Certificates service
* Support to create child tenancies in an organization and manage subscriptions in the Organizations service
* Support for Certificates service integration in the Load Balancing service
* Support for creating hosts in specific availability domains in the VMWare Solution service
* Support for user-defined functions and libraries, as well as scheduling and orchestration, in the Data Integration service
* Support for EM-managed Exadatas and EM-managed hosts in the Operations Insights service

Breaking
--------
* Models `ComputeInstanceGroupBlueGreenDeployStageExecutionProgress`, `ComputeInstanceGroupBlueGreenTrafficShiftDeployStageExecutionProgress`, `ComputeInstanceGroupCanaryApprovalDeployStageExecutionProgress`, `ComputeInstanceGroupCanaryDeployStageExecutionProgress`, `ComputeInstanceGroupCanaryTrafficShiftDeployStageExecutionProgress`, `RunPipelineDeployStageExecutionProgress`and `RunValidationTestOnComputeInstanceDeployStageExecutionProgress` were removed from the DevOps service.

====================
2.48.0 - 2021-10-19
====================

Added
-----
* Support for creating database systems from backups with database software images in the Database service
* Support for optionally providing a SID prefix during Exadata database creation in the Database service
* Support for node subsetting on VM clusters in the Database service
* Support for non-CDB to PDB conversion in the Database service
* Support for default homepages, unprocessed data buckets, and parsing geostats in the Logging Analytics service
* Support for Circuit Breakers. Please refer `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/circuit_breakers.html>`__ to learn more.
* Support for enabling/disabling Retries globally for operations using Default Retry Strategy. Please refer `here <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html#overriding-the-retry-behavior-at-global-sdk-level>`__ for more info.

Breaking
--------
* Default Retry strategy will now retry operations for max 8 attempts and have a timeout of 600 seconds before failing. The strategy will now use `De-Correlated jitter <https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/retries.html#de-correlated-jitter>`__ as the default delay strategy.

====================
2.47.1 - 2021-10-12
====================

Added
-----
* Support for the Data Labeling Service
* Support for the Web Application Firewall service
* Support for querying and setting Application Performance Monitoring configurations in the Application Performance Monitoring service
* Support for the run-once monitor feature and network data collection in the Application Performance Monitoring service
* Support for Oracle Enterprise Manager bridges, source auto-association, source event types mapping, and partitioning and searching data by LogSet in the Logging Analytics service
* Support for Log events APIs used by plugins like fluentd, fluentbit, etc. to upload data in the Logging Analytics service
* Support for a new ActionType: FAILED in work requests in the VMware Provisioning service
* Support for calling Oracle Cloud Infrastructure services in the il-jerusalem-1 region

====================
2.47.0 - 2021-10-05
====================

Added
-----
* Support for configuring Binlog variables in the MySQL Database service.
* Support new response value "OPERATOR" for backup creationType in list and get MDS backup API in the MySQL Database service.
* Support for SetAutoUpgradableConfig and GetAutoUpgradableConfig operations in Management Agent Cloud service.
* Support for additional installType filter for List Management Agents, Images and Count API operations in Management Agent Cloud service.
* Support for list and read DeploymentUpgrade, cancel and restore DeploymentBackup in the Golden Gate service.
* Support for non-autonomous databases targets, executing Pre-Migration advisor, uploading Datapump logs into Object Storage bucket, and filtering Database Objects in the Database Migration service.
* Support for calling Oracle Cloud Infrastructure services in the ap-ibaraki-1 region.

Breaking changes
----
* Param `is_agent_auto_upgradable` is removed from model `UpdateManagementAgentDetails` in the Management Agent Cloud Service
* Param `display_name` is removed from operations `list_work_requests`, `list_work_request_logs` and `list_work_request_errors` in the Database Migration Service Client
* Allowed values for param `sort_order` from operation `list_work_requests` changed to `timeAccepted` in the Database Migration Service Client
* Allowed values for param `sort_order` from operations `list_work_request_errors` and `list_work_request_logs` changed to `timestamp` in the Database Migration Service Client
* Param `time_stamp` renamed to `timestamp` in models `WorkRequestLogEntry`, `WorkRequestError` for the Database Migration Service
* Param `compartment_id` is removed from model `UpdateAgentDetails` for the Database Migration Service

====================
2.46.0 - 2021-09-28
====================

Added
-----
* Support for autonomous databases and clones on shared infrastructure not requiring mTLS in the Database service
* Support for server-side encryption using object-specific KMS keys in the Object Storage service
* Support for Windows in the Java Management service
* Support for using network security groups in the API Gateway service
* Support for network security groups in the Functions service
* Support for signed container images in the Functions service
* Support for setting message format when creating and updating alarms in the Monitoring service
* Support for user and security assessment features in the Data Safe service

Breaking
--------
* Operations `request_summarized_application_usage`, `request_summarized_installation_usage`, `request_summarized_jre_usage`, `request_summarized_managed_instance_usage` were removed from the Java Management Service Client
* Models `RequestSummarizedApplicationUsageDetails`, `RequestSummarizedInstallationUsageDetails`, `RequestSummarizedJreUsageDetails` and `RequestSummarizedManagedInstanceUsageDetails` were removed from Java Management Service

Changed
-------
* Dependency `configparser` will only be installed for Python 2. The built-in configparser will be used for Python 3

====================
2.45.1 - 2021-09-14
====================

Added
-----
* Support for serviceHostKeyFingerprint property for InstanceConsoleConnection in Core service
* Support for Shielded Instances in Core service
* Support for ML Jobs in the Data Science service

====================
2.45.0 - 2021-09-07
====================

Added
-----
* Support for terraform advanced options (detailed log level, refresh, and parallelism) on jobs in the Resource Manager service
* Support for forced cancellation when cancelling jobs in the Resource Manager service
* Support for getting the detailed log content of a job in the Resource Manager service
* Support for provider information in the responses of list operations in the Management Dashboard service
* Support for scheduled jobs in Database Management service
* Support for monitoring and management of OCI virtual machine, bare metal, and ExaCS databases in the Database Management service
* Support for a unified way of managing both external and cloud databases in the Database Management service
* Support for metrics and Performance Hub on virtual machine, bare metal, and ExaCS databases in the Database Management service

Breaking
--------
* Param `oci_splat_generated_ocids` is removed from operation `create_template` in the Resource Manager service

====================
2.44.2 - 2021-08-31
====================

Added
-----
* Support for Oracle Analytics Cloud and OCI Vault integration on connections in the Data Catalog service
* Support for critical event monitoring in the OS Management service

====================
2.44.1 - 2021-08-24
====================

Added
-----
* Support for generating recommended VM cluster networks in the Database service
* Support for creating VM cluster networks with a specified listener port in the Database service

====================
2.44.0 - 2021-08-17
====================

Added
-----
* Support for getting management agent hosts which are eligible to create Operations Insights host resources on, in the Operations Insights service
* Support for getting summarized agent counts and summarized plugin counts in the Management Agent Cloud service

Breaking
--------
* Model `WorkSubmissionKey` was removed from Management Agent Cloud service
* Type for parameter `plugin_name` changed to `list[str]` from `str` in operation `list_management_agent_plugins` in the Management Agent Cloud Service
* Type for parameter `version` changed to `list[str]` from `str` in operation `list_management_agent_plugins` in the Management Agent Cloud Service
* Type for parameter `platform_type` changed to `list[str]` from `str` in operation `list_management_agent_plugins` in the Management Agent Cloud Service

====================
2.43.2 - 2021-08-03
====================

Added
-----
* Support for manually copying volume group backups across regions in the Block Volume service
* Support for work requests for the copy volume backup and copy boot volume backup operations in the Block Volume service
* Support for specifying external Hive metastores during application creation in the Data Flow service
* Support for changing the compartment of a backup in the MySQL Database service
* Support for model catalog features including provenance, metadata, schemas, and artifact introspection in the Data Science service
* Support for Exadata system network bonding in the Database service
* Support for creating autonomous databases with early patching enabled in the Database service

====================
2.43.1 - 2021-07-27
====================

Added
-----
* Support for filtering by tag on capacity planning and SQL warehouse list operations in the Operations Insights service
* Support for creating cross-region autonomous data guards in the Database service
* Support for the customer contacts feature on cloud exadata infrastructure in the Database service
* Support for cost analysis custom tables in the Usage service

====================
2.43.0 - 2021-07-20
====================

Added
-----
* Support for schedules, schedule tasks, REST tasks, operators, S3, and Fusion Apps in the Data Integration service
* Support for getting available updates and update histories for VM clusters in the Database service
* Support for downloading network validation reports for Exadata network resources in the Database service
* Support for patch and upgrade of Grid Infrastructure (GI), and update of DomU OS software for VM clusters in the Database service
* Support for updating data guard associations in the Database service

Changed
-------
* Changed Expect HTTP header to support only Object Storage and Log Analytics services, to mitigate performance degradation issues in the OCI Python SDK v2.38.4 and above. For more information, please see https://github.com/oracle/oci-python-sdk/issues/367

Breaking
--------
* Data Type for param `type` changed from `str` to `object` in model `ShapeField` in the Data Integration Service
* Data Type for param `type` changed from `oci.data_integration.models.BaseType` to `object` in model `Parameter` in the Data Integration Service
* Data Type for param `type` changed from `str` to `object` in model `NativeShapeField` in the Data Integration Service
* Base class for model `OracleWriteAttributes` changed from `object` to `oci.data_integration.models.AbstractWriteAttribute` in the Data Integration Service
* Base class for model `OracleReadAttributes` changed from `object` to `oci.data_integration.models.AbstractReadAttribute` in the Data Integration Service
* Base class for model `OracleAdwcWriteAttributes` changed from `object` to `oci.data_integration.models.AbstractWriteAttribute` in the Data Integration Service
* Base class for model `OracleAtpWriteAttributes` changed from `object` to `oci.data_integration.models.AbstractWriteAttribute` in the Data Integration Service
* Param `bucket_name` was removed from model `OracleAtpWriteAttributes` in the Data Integration Service
* Param `bucket_name` was removed from model `OracleAdwcWriteAttributes` in the Data Integration Service
* Param `bucket_name` was removed from model `OracleAdwcWriteAttributes` in the Data Integration Service
* Param `is_file_pattern` was removed from model `CsvFormatAttribute` in the Data Integration Service
* Constant `MODEL_TYPE_REST_OPERATOR` was removed from model `Operator` in the Data Integration Service

====================
2.42.0 - 2021-07-13
====================

Added
-----
* Support for the AI Anomaly Detection service
* Support for retrieving a DNS zone as a zone file in the DNS service
* Support for querying manual adjustments in the Usage service
* Support for searching Marketplace listings in the Marketplace service
* Support for new cluster type 'ODH' in the Big Data service
* Support for availability domain as an optional parameter when creating VLANs in the Networking service
* Support for search domain type on DHCP options, to support multi-level domain search in the Networking service

Breaking
--------
* Model `TSIG` was removed from the DNS service
* Param `tsig` was removed from model `ExternalMaster` in the DNS service
* Models `CreateCustomTableDetails`, `CreateScheduleReportDetails`, `CustomTable`, `CustomTableCollection`, `CustomTableSummary`, `SavedScheduleReport`, `ScheduleReport`, `ScheduleReportCollection`, `ScheduleReportSummary`, `UpdateCustomTableDetails`, `UpdateScheduleReportDetails` were removed from Usage API service

====================
2.41.1 - 2021-07-06
====================

Added
-----
* Support for order activation in the Organizations service
* Support for resource principal authorization on Enterprise Manager bridge resources in the Operations Insights service
* Support for the starter edition license type in the Content and Experience service
* Support for the Generic Artifacts service's new domain name

====================
2.41.0 - 2021-06-29
====================

Added
-----
* Support for the DevOps service
* Support for configuring network security groups for node pools in the Container Engine for Kubernetes service
* Support for optionally specifying CPU core count and data storage size when creating autonomous databases in the Database service
* Support for metastore and initial data asset import/export in the Data Catalog service
* Support for associating domain names to emails and managing email domain names / DKIM in the Email Delivery service
* Support for email domain names on senders and suppressions in the Email Delivery service
* Support for signing request bodies for PUT/POST/PATCH requests where it is expected by the service. For more information, please see https://docs.oracle.com/en-us/iaas/tools/python/latest/sdk_behaviors/index.html

Breaking
--------
* The property `cpu_core_count` was made optional in model CreateAutonomousDatabaseBase in the Database service
* `DISPLAYNAME` was removed as allowed value for the SortBy property in method `list_job_executions` under the Data Catalog service
* Util function `should_record_body_position_for_retry` was moved from src/oci/retry/retry_utils.py to src/oci/util.py
* Util function `record_body_position_for_retry` was renamed to `record_body_position_for_rewind` and was moved from src/oci/retry/retry_utils.py to src/oci/util.py
* Util function `rewind_body_for_retry` was renamed to `rewind_body` and was moved from src/oci/retry/retry_utils.py to src/oci/util.py

====================
2.40.1 - 2021-06-22
====================

Added
-----
* Support for virtual machine and bare metal pluggable databases in the Database service

Changed
-------
* Changed allowed versions of cryptography package to a range, starting from from 3.2.1 up to 3.4.7

====================
2.40.0 - 2021-06-15
====================

Added
-----
* Support for elastic storage on Exadata Infrastructure resources for Cloud at Customer in the Database service
* Support for registration and management of target databases in the Data Safe service
* Support for config on metadata in the Management Dashboard service
* Support for a new work request operation type for node pool reconciliation events in the Container Engine for Kubernetes service
* Support for migrating clusters with a public Kubernetes API endpoint which are not integrated with a customer's VCN to a VCN-native cluster in the Container Engine for Kubernetes service
* Support for getting the spark version of applications, and filtering applications by spark version, in the Data Flow service

Breaking
--------
* The properties `freeform_tags` and `defined_tags` were removed from the ManagementDashboardExportDetails model in the Management Dashboard service

====================
2.39.1 - 2021-06-08
====================

Added
-----
* Support for Java Management service
* Support for resource principals for the Enterprise Manager bridge resource in Operations Insights service
* Support for encryptionInTransitType in BootVolumeAttachment and IScsiVolumeAttachment in Core service
* Support for updating iscsiLoginState for VolumeAttachment in Core service
* Support for a new type of Source called Import for use with the Export tool in Application Migration service

Fixed
-----
* Fixed a bug where requests were not retried for a specific case of Upload Manager uploading a file with multipart disabled and callback provided

====================
2.39.0 - 2021-06-01
====================

Added
-----
* Support for configuration of autonomous database KMS keys in the Database service
* Support for creating database software images with any supported RUs in the Database service
* Support for creating database software images from an existing database home in the Database service
* Support for listing all NSGs associated with a given VLAN in the Networking service
* Support for a duration windows, task failure reasons, and next execution times on scheduled tasks in the Logging Analytics service
* Support for calling Oracle Cloud Infrastructure services in the sa-vinhedo-1 region

Breaking
-----
* `compartment_id` is now optional in operation `list_network_security_groups` in the Networking service

====================
2.38.4 - 2021-05-25
====================

Added
-----
* Support for the Generic Artifacts service
* Support for the Bastion service
* Support for reading secrets by name in the Vault service
* Support for the isDynamic field when listing definitions in the Limits service
* Support for getting billable image sizes in the Compute service
* Support for getting Automatic Workload Repository (AWR) data on external databases in the Database Management service
* Support for the VM.Standard.E3.Flex flexible compute shape with customizable OCPUs and memory on notebooks in the Data Science service
* Support for container images and generic artifacts billing in the Registry service
* Support for the HCX Enterprise add-on in the VMware Solution service
* Support for the Expect HTTP header. Expect headers are added by default for all PUT/POST operations

====================
2.38.3 - 2021-05-18
====================

Added
-----
* Support for spark-submit compatible options in the Data Flow service
* Support for Object Storage as a configuration source in the Resource Manager service

====================
2.38.2 - 2021-05-11
====================

Added
-----
* Support for creating notebook sessions with larger block volumes in the Data Science service
* Support for database maintenance run patch modes in the Database service

Fixed
-----
* Fixed a bug where `timeout=None` was not respected when passed to clients. The older versions of the SDK still use the default connection timeout(10s) and read timeout(60s) when initialized with `timeout=None`

Changed
-------
* Improvement in the performance of Upload Manager for parallel uploads. This is achieved by overriding the default read size of Python HTTP client from 8192 bytes to 64 kb.

====================
2.38.1 - 2021-05-04
====================

Added
-----
* Support for the Operator Access Control service
* Support for the Service Catalog service
* Support for the AI Language service
* Support for autonomous database on Exadata Cloud at Customer infrastructure patching in the Database service

====================
2.38.0 - 2021-04-27
====================

Added
-----
* Support for RACs (real application clusters) for external container, non-container, and pluggable databases in the Database service
* Support for data masking in the Cloud Guard service
* Support for opting out of DNS records during instance launch, as well as attaching secondary VNICs, in the Compute service
* Support for mutable sizes on cluster networks in the Autoscaling service
* Support for auto-tiering on buckets in the Object Storage service

Breaking
--------
* VCN id parameters were moved from being required to being optional on all list operations in the Networking service

====================
2.37.0 - 2021-04-20
====================

Added
-----
* Support for opting in/out of live migration on instances in the Compute service
* Support for enabling/disabling Operations Insights on external non-container and external pluggable databases in the Database service
* Support for a GraphStudio URL as a connection URL on databases in the Database service
* Support for adding customer contacts on autonomous databases in the Database service
* Support for name annotations on harvested objects in the Data Catalog service

Changed
-------
* If retries are enabled, the SDK will now retry on status 409/IncorrectState. It will not retry on status 501.

Breaking
--------
* Bumped cryptography version to 3.3.2 to address security vulnerability https://github.com/oracle/oci-python-sdk/pull/322

====================
2.36.0 - 2021-04-13
====================

Added
-----
* Support for the Database Migration service
* Support for the Networking Topology service
* Support for getting the id of peered VCNs on local peering gateways in the Networking service
* Support for burstable instances in the Compute service
* Support for preemptible instances in the Compute service
* Support for fractional resource usage and availability in the Limits service
* Support for streaming analytics in the Service Connector Hub service
* Support for flexible routing inside DRGs to enable packet flow between any two attachments in the Networking service
* Support for routing policy to customize dynamic import/export of routes in the Networking service
* Support for IPv6, including on FastConnect and IPsec resources, in the Networking service
* Support for request validation policies in the API Gateway service
* Support for RESP-compliant (e.g. REDIS) response caches, and for configuring response caching per-route in the API Gateway service
* Support for flexible billing in the VMWare Solution service
* Support for new DNS format for the Web Application Acceleration and Security service
* Support for configuring APM tracing on applications and functions in the Functions service
* Support for Enterprise Manager external databases and Management Agent Service managed external databases and hosts in the Operations Insights service
* Support for getting cluster cache metrics for RAC CDB managed databases in the Database Management service

Breaking changes
----
* Removed response codes `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307` and `444` from attribute `block_response_code` in model `AddressRateLimiting` in the Web Application Acceleration and Security Service
* `VcnId` was made optional in CreateDrgAttachmentDetails model under Core services.
* The property `IsInternetAccessAllowed` was removed from CreateIpv6Details model under Core services.
* The property `Ipv6CidrBlock` was removed from CreateVcnDetails model under Core services.
* The property `PublicIpAddress` and `IsInternetAccessAllowed` were removed from Ipv6 model under Core services.
* Required property `PeerId` was added to LocalPeeringGateway model under Core services.
* The property `Ipv6PublicCidrBlock` was removed from Subnet model under Core services.
* The property `Ipv6PublicCidrBlock` was replaced by `Ipv6CidrBlocks` in Vcn model in Core services.
* Required property `CurrentSku` was added under CreateEsxiHostDetails under Ocvp service.
* Required property `InitialSku` was added under CreateSddcDetails under Ocvp service.
* Required properties `BillingContractEndDate`, `NextSku` & `CurrentSku` were added under EsxiHost under Ocvp service.
* Required properties `BillingContractEndDate`, `NextSku` & `CurrentSku` were added under EsxiHostSummary under Ocvp service.
* Required property `InitialSku` was added under Sddc under Ocvp service.
* Required property `Id` was added under DatabaseDetails under Opsi service.
* `compartment_id` and `database_id` are now optional in operation `ingest_sql_bucket` under Opsi service.
* `compartment_id` and `database_id` are now optional in operation `ingest_sql_plan_lines` under Opsi service.
* `compartment_id` and `database_id` are now optional in operation `ingest_sql_text` under Opsi service.
* `compartment_id` is now optional in operation `list_database_insights` under Opsi service.
* `database_id` is now optional in operation `list_sql_plans` under Opsi service.
* `database_id` is now optional in operation `summarize_sql_response_time_distributions` under Opsi service.
* `database_id` is now optional in operation `summarize_sql_statistics_time_series_by_plan` under Opsi service.
* `database_id` is now optional in operation `summarize_sql_plan_insights` under Opsi service.
* Value of attribute `model_type` in model `ConnectionDetails` in Data Integration service defaults to UNKNOWN_ENUM_VALUE when it receives an invalid value. In the earlier versions, this raises a ValueError

====================
2.35.1 - 2021-04-06
====================

Added
-----
* Support for scheduling the suspension and resumption of compute instance pools based on predefined schedules in the Autoscaling service
* Support for database software images for Cloud@Customer in the Database service
* Support for OCIC IDCS authorization details in the Application Migration service
* Support for cross-region asynchronous volume replication in the Block Storage service
* Support for SDK generation in the API Gateway service
* Support for container image signing in the Registry service
* Support for cluster features as a part of the Container Engine for Kubernetes service
* Support for filtering dedicated virtual machine hosts by remaining memory and OCPUs in the Compute service
* Support for read/write-any object from buckets using pre-authenticated requests in the Object Storage service
* Support for restricting pre-authenticated requests by prefix in the Object Storage service
* Support for route filtering on public virtual circuits in the Virtual Networking service
* Support for calculating content length of a non-resettable stream for binary uploads. A non-resettable stream will be buffered into memory to calculate the content length. A buffer_limit may be passed into the request to provide a buffer limit. The default buffer limit is 100 MiB. More documentation can be found here: https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/sdk_behaviors/index.html

====================
2.35.0 - 2021-03-30
====================

Added
-----
* Support for the Vulnerability Scanning service
* Support for vSphere 7.0 in the VMware Solution service
* Support for forecasting in the Usage service
* Support for viewing, searching, and modifying parameters for on-premise Oracle databases in the Database Management service
* Support for listing tablespaces of managed databases in the Database Management service
* Support for cross-regional replication of keys in the Key Management service
* Support for highly-available database systems in the MySQL Database service
* Support for Oracle Enterprise Manager bridges, source auto-association, source event type mappings, and plugins to upload data in the Logging Analytics service

Breaking
--------
* Name of Enum attribute "forcast_type" in Usage API service renamed to "forecast_type"
* Value of Enum attribute "forecast_type" in Usage API service defaults to UNKNOWN_ENUM_VALUE when it receives an invalid value. In the earlier versions, this raises a ValueError
* Retries are now enabled in Upload Manager. The SDK used to explicitly override retry configuration on binary upload operations because of potential data corruption issue (https://github.com/oracle/oci-python-sdk/issues/203).

====================
2.34.0 - 2021-03-23
====================

Added
-----
* Support for the Network Load Balancing service
* Support for maintenance runs on autonomous databases in the Database service
* Support for announcement preferences in the Announcements service
* Support for domain claiming in the Organizations service
* Support for saved reports in the Usage service
* Support for the HeatWave in-memory analytics accelerator in the MySQL Database service
* Support for community applications in the Marketplace service
* Support for capacity reservations in the Compute service

Breaking
--------
* Parameter `vnic_id` changed from optional to required in model `CreateIpv6Details` in the core services
* Parameter `vnic_id` changed from optional to required in model `Ipv6` in the core services
* Value of Enum attribute `operator` in Usage API service defaults to `UNKNOWN_ENUM_VALUE` when it receives an invalid value. In the earlier versions, this raises a `ValueError`

====================
2.33.0 - 2021-03-16
====================

Added
-----
* Support for routing policies and HTTP2 listener protocols in the Load Balancing service
* Support for model deployments in the Data Science service
* Support for private clusters in the Container Engine for Kubernetes service
* Support for updating an instance's usage type in the Content and Experience service

Breaking
--------
* Retries are now enabled on all operations performing binary data upload, except upload manager. The SDK used to explicitly override retry configuration on binary upload operations because of potential data corruption issue (https://github.com/oracle/oci-python-sdk/issues/203).

====================
2.32.1 - 2021-03-09
====================

Added
-----
* Support for the Application Performance Monitoring service
* Support for the Golden Gate service
* Support for SMS subscriptions in the Notifications service
* Support for friendly-formatted messages in the Service Connector Hub service
* Support for attaching and detaching instances to instance pools in the Autoscaling service

====================
2.32.0 - 2021-03-02
====================

Added
-----
* Support for pipelines, pipeline tasks, and favorites in the Data Integration service
* Support for publishing tasks to OCI Data Flow in the Data Integration service
* Support for clones in the File Storage service

Breaking
--------
* Changed model `UniqueKey` in the Dataintegration service to not inherit from Key.
* Changed model `PrimaryKey` in the Dataintegration service to inherit from `UniqueKey`.
* Removed enum values `PRIMARY_KEY` and `UNIQUE_KEY` in property `model_type` from model `key` in the Dataintegration service.

====================
2.31.2 - 2021-02-23
====================

Added
-----
* Support for the OCI Registry service
* Support for exporting an existing running VM, or a copy of VM, into a VMDK, QCOW2, VDI, VHD, or OCI formatted image in the Compute service
* Support for platform configurations on instances in the Compute service
* Support for providing target tags and target compartments on profiles in the Optimizer service
* Support for the 'Fix it' feature in the Optimizer service

====================
2.31.1 - 2021-02-16
====================

Added
-----
* Support for scan DNS names and zone ids on database system, cloud VM cluster, and autonomous Exadata infrastructure responses in the Database service
* Support for specifying ACL rules to limit ingress into public load balancers in the Integration service
* Support for Cloud at Customer as a source type in the Application Migration service
* Support for selective migration of specific resources in the Application Migration service

====================
2.31.0 - 2021-02-09
====================

Added
-----
* Support for the Database Management service
* Support for setting an offset for budget processing in the Budgets service
* Support for enabling and disabling Oracle Cloud Agent plugins in the Compute service
* Support for listing available plugins and for getting the status of plugins in the Oracle Cloud Agent service
* Support for one-off patching in autonomous transaction processing - dedicated databases in the Database service
* Support for additional database upgrade options in the Database service
* Support for glossary term recommendations in the Data Catalog service
* Support for listing errata in the OS Management service

Breaking
--------
* Model `InstanceAgentCommandContentInfo` is removed from Compute Instance Agent service

====================
2.30.0 - 2021-02-02
====================

Added
-----
* Support for checking if a contact for Exadata infrastructure is valid in My Oracle Support in the Database service
* Support for checking if Exadata infrastructure is in a degraded state in the Database service
* Support for updating the operating system on a VM cluster in the Database service
* Support for external databases in the Database service
* Support for uploading objects to the infrequent access storage tier in the Object Storage service
* Support for changing the storage tier of existing objects in the Object Storage service
* Support for private templates in the Resource Manager service
* Support for multiple encryption domains on IPSec tunnels in the Networking service

Breaking
--------
* Attribute `vnic_id` in response model `Ipv6` changed from required to optional in the Networking service

====================
2.29.0 - 2021-01-26
====================

Added
-----
* Support for creating, managing, and using asymmetric keys in the Key Management service
* Support for peer ACD unique names in Exadata Cloud at Customer in the Database service
* Support for ACLs on autonomous databases in Exadata Cloud at Customer Data Guard in the Database service
* Support for drift detection on individual resources of a stack in the Resource Manager service
* Support for private access channels and vanity URLs in the Analytics Cloud service
* Support for updating load balancer shapes in the Blockchain Platform service
* Support for assigning volume backup policies to volume groups in the Block Volume service

Breaking
--------
* Parameter `idcs_access_token` in model `CreateBlockchainPlatformDetails` changed from optional to required in the Blockchain service

====================
2.28.0 - 2021-01-19
====================

Added
-----
* Support for Logging Analytics as a target in the Service Connector Hub service
* Support for lookups, agent collection warnings, task commands, and data archive/recall in the Logging Analytics service

Fixed
-----
* Fixed a bug in the endpoint used for the Management Dashboard service

Breaking
--------
* A new required property `kind` is added to the models `UpdateScheduledTaskDetails` and `ScheduledTask` in the Log Analytics service
* The allowed values for parameter `sort_by` are restricted for methods `list_meta_source_types`, `list_parser_functions`, `list_parser_meta_plugins`, `list_source_label_operators`, `list_source_meta_functions` in the Log Analytics service. For more information please see the documentation for `LogAnalyticsClient <https://docs.oracle.com/en-us/iaas/tools/python/latest/api/log_analytics/client/oci.log_analytics.LogAnalyticsClient.html#loganalyticsclient>`_

====================
2.27.0 - 2021-01-12
====================

Added
-----
* Support for auto-scaling in the Big Data service
* Documentation fixes for the Logging Search service

Breaking
--------
* Removed `LIFECYCLE_STATE_UPDATING_INFRA` from model BdsInstance in the Big Data service
* Removed `LIFECYCLE_STATE_STOPPING` and `LIFECYCLE_STATE_STARTING` from model Node in the Big Data Service

====================
2.26.0 - 2020-12-15
====================

Added
-----
* Support for filtering listKeys based on KeyShape in KeyManagement service
* Support for the Oracle Roving Edge Infrastructure service
* Support for flexible ShapeDetails in Load Balancer service
* Support for listing of harvested Rules, additional filtering for Logical Entity list calls in Data Catalog service
* Support second level domain for audit SDK
* Support for listing flex components in Database service
* Support for APEX service for ADBS on OCI console for Database service
* Support for Customer-Managed Key features as a part of the Database service
* Support for Github configuration source provider as part of the Resource Manager service

Breaking
--------
* Removed deprecated create_autonomous_data_warehouse API from Database service
* Removed deprecated create_autonomous_data_warehouse_backup API from Database service
* Removed deprecated delete_autonomous_data_warehouse API from Database service
* Removed deprecated generate_autonomous_data_warehouse_wallet API from Database service
* Removed deprecated get_autonomous_data_warehouse API from Database service
* Removed deprecated get_autonomous_data_warehouse_backup API from Database service
* Removed deprecated list_autonomous_data_warehouse_backups API from Database service
* Removed deprecated list_autonomous_data_warehouses API from Database service
* Removed deprecated restore_autonomous_data_warehouse API from Database service
* Removed deprecated start_autonomous_data_warehouse API from Database service
* Removed deprecated stop_autonomous_data_warehouse API from Database service
* Removed deprecated update_autonomous_data_warehouse API from Database service
* The enum attributes `lifecycle_state` and `license_model` from Model `AutonomousDataWarehouseSummary` in the Database service raise `ValueError` if they receive an invalid value. In the earlier versions, the value defaults to `UNKNOWN_ENUM_VALUE`.
* The enum attributes `lifecycle_state` and `license_model` from Model `AutonomousDataWarehouse` in the Database service raise `ValueError` if they receive an invalid value. In the earlier versions, the value defaults to `UNKNOWN_ENUM_VALUE`.

Fixed
-----
* Fixed an issue in the documentation where model links were incorrect

====================
2.25.1 - 2020-12-08
====================

Added
-----
* Support for Integration Service custom endpoint feature
* Support for metadata field in IdentityProvider Get and List response
* Support for fine-grained data analysis and improved SQL insights
* Support for ADB Dedicated - ORDS and SSL cert rotation at AEI
* Support for Maintenance Schedule feature for Exadata Infrastructure resources for ExaCC

====================
2.25.0 - 2020-12-01
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the sa-santiago-1 region
* Support for peer and OSN resources, as well as retry tokens, in the Blockchain Platform service
* Support for getting the availability status of management agents in the Management Agent service
* Support for the on-prem-connector resource type in the Data Safe service
* Support for service channels in the MySQL Database service
* Support for getting the creation type of backups, and for filtering backups by creation type in the MySQL Database service

Breaking
--------
* Parameter `compartment_id` changed from optional to required for method `list_work_requests` in the Data Safe service
* Return type of method `create_data_safe_private_endpoint` changed from `None` to `oci.data_safe.models.DataSafePrivateEndpoint` in the Data Safe service
* Parameters `freeform_tags` and `defined_tags` are removed from model `EnableDataSafeConfigurationDetails` in the Data Safe service

====================
2.24.1 - 2020-11-24
====================

Added
-----
* Provide example for pagination that creates a *Details object for pagination
* Provide example to turn response and model to JSON

Security
-----
* cryptography pinning to cryptography=3.2.1 to address vulnerability `Github security alerts <https://github.com/oracle/oci-python-sdk/pull/299>`__

====================
2.24.0 - 2020-11-17
====================

Added
-----
* Support for specifying memory for AMD E3 shapes during node pool creation and update in the Container Engine for Kubernetes service
* Support for upgrading a database on a VM database system in the Database service
* Support for listing autonomous database clones in the Database service
* Support for Data Guard with autonomous container databases on Exadata Cloud at Customer in the Database service
* Support for getting the last login time of a user in the Identity service
* Support to bulk editing tags on resources in the Identity service

Breaking
--------
* The models `AgentUpload`, `Attribute`, `CreateNamespaceDetails`, `FieldMap`, `GenerateAgentObjectNameDetails`, `LogAnalytics`, `LogAnalyticsCollectionWarning`, `LogAnalyticsSummary`, `OutOfBoxEntityTypeDetails`, `Query`, `QueryWorkRequestResource`, `RegisterEntityTypesDetails`, `ServiceTenancy`, `StringListDetails` are removed from the Log Analytics service
* The enum `name` removed value `CUSLTER_SPLIT` and added `CLUSTER_SPLIT` in the Log Analytics service
* The value for enum `status` is not validated against allowed values and will not raise `ValueError` in the Container Engine service

====================
2.23.5 - 2020-11-10
====================

Added
-----
* Support for the 21C autonomous database version in the Database service
* Support for creating a Data Guard association with a standby database from a database software image in the Database service
* Support for specifying a TDE wallet password when creating a database or database system in the Database service
* Support for enabling access control lists for autonomous databases on Exadata Cloud At Customer in the Database service
* Support for private DNS resolvers, resolver endpoints, and views in the DNS service
* Support for getting a VCN and resolver association in the Networking service
* Support for additional parameters when updating subnets and VLANs in the Networking service
* Support for analytics clusters (database accelerators) in the MySQL Database service
* Support for migrations to Java Cloud Service and Oracle Weblogic Server instances that use existing databases in the Application Migration service
* Support for specifying reserved IPs when creating load balancers in the Load Balancing service

Changed
-------
* Removed support for Python 3.5, since it is end of life
* Support for Python 3.7, 3.8 and 3.9

====================
2.23.4 - 2020-11-03
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the uk-cardiff-1 region
* Support for the Organizations service
* Support for the Optimizer service
* Support for tenancy ID and name on responses in the Usage service
* Support for object versioning in object lifecycle management in the Object Storage service
* Support for specifying a syslog URL for applications in the Functions service
* Support for creation of always-free NoSQL database tables in the NoSQL Database service

====================
2.23.3 - 2020-10-29
====================

Fixed
-------
* Fixed an issue where `UploadManager.upload_stream()` raised `MultipartUploadError` if the time to upload is greater than the read timeout. Please see `github issue #300 <https://github.com/oracle/oci-python-sdk/issues/300>`_ for more details.

====================
2.23.2 - 2020-10-27
====================

Added
-----
* Support for the Compute Instance Agent service
* Support for key store resources and operations in the Database service
* Support for specifying a key store when creating autonomous container databases in the Database service

Fixed
-------
* Bypassed the use of PyOpenSSL in the vendored requests library only if ssl does not have SNI. This may fix a `known issue <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/known-issues.html#uploadmanager-generates-ssl3-write-pending-error-when-a-read-timeout-is-set-for-the-object-storage-client>`_. depending on your environment. For more information, please see the link to the docs.

====================
2.23.1 - 2020-10-20
====================

Added
-----
* Support for the Operations Insights service
* Support for updating autonomous databases to enable/disable Operations Insights service integration, in the Database service
* Support for the NEEDS_ATTENTION lifecycle state on database systems in the Database service
* Support for HCX in the VMware Solutions service
* Added an example script for Usage API

====================
2.23.0 - 2020-10-13
====================

Added
-----
* Support for API definitions in the API Gateway service
* Support for pattern-based logical entities, namespace-bound custom properties, and faceted search in the Data Catalog service
* Support for autonomous Data Guard on autonomous infrastructure in the Database service
* Support for creating a Data Guard association on an existing standby database home in the Database service
* Support for upgrading cloud VM cluster grid infrastructure in the Database service

Breaking
--------
* Attribute `is_quick_start` in models `CreateLogSavedSearchDetails`, `LogSavedSearchSummary` and `LogSavedSearch` is removed from the Logging Management service
* Lifecycle State `DELETED` is removed from the Logging Management service

====================
2.22.0 - 2020-10-06
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the me-dubai-1 region
* Support for rotating keys on autonomous container databases and autonomous databases in the Database service
* Support for cloud Exadata infrastructure and cloud VM clusters in the Database service
* Support for controlling the display of tax banners in the Marketplace service
* Support for application references, patch changes, generic JDBC and MySQL data asset types, and publishing tasks to OCI Dataflow in the Data Integration service
* Support for disabling the legacy Instance Metadata endpoints v1 in the Compute service
* Support for instance configurations specifying instance options in the Compute Management service

Breaking
--------
* The attribute `model_type` in `TypedObject` model now raises `ValueError` when provided with an invalid value. Please see the `documentation <https://docs.cloud.oracle.com/en-us/iaas/tools/python/2.21.6/api/data_integration/models/oci.data_integration.models.TypedObject.html#oci.data_integration.models.TypedObject.model_type>`_ for a list of allowed values.

====================
2.21.6 - 2020-09-29
====================

Added
-----
* Support for specifying custom content dispositions when downloading objects in the Object Storage service
* Support for the “bring your own IP address” feature in the Virtual Networking service
* Support for updating the tags of instance console connections in the Compute service
* Support for custom SSL certificates on gateways in the API Gateway service

====================
2.21.5 - 2020-09-22
====================

Added
-----
* Support for software keys in the Key Management service
* Support for customer contacts on Exadata Cloud at Customer in the Database service
* Support for updating open modes and permission levels of autonomous databases in the Database service
* Support for flexible memory on VM instances in the Compute and Compute Management services

====================
2.21.4 - 2020-09-15
====================

Added
-----
* Support for the Cloud Guard service
* Support for specifying desired consumption models when creating instances in the Integration service
* Support for dynamic shapes in the Load Balancing service

====================
2.21.3 - 2020-09-08
====================

Added
-----
* Support for Logging Service
* Support for Logging Analytics Service
* Support for Logging Search Service
* Support for Logging Ingestion Service
* Support for Management Agent Cloud Service
* Support for Management Dashboard Service
* Support for Service Connector Hub service
* Support for Policy based Request/Response transformation in the API Gateway Service
* Support for sending diagnostic interrupt to a VM instance in the Compute Service
* Support for custom Database Software Images in the Database Service
* Support for getting and listing container database patches for Autonomous Container Database resources in the Database Service
* Support for updating patch id on maintenance run for Autonomous Container Database resources in the Database Service
* Support for searching Oracle Cloud resources across tenancies in the Search Service
* Documentation update for Logging Policies in the API Gateway service
* Support for Python SDK in Cloud Shell

====================
2.21.1 - 2020-08-18
====================

Added
-----
* Support for custom boot volume size and other node pool updates in the Container Engine for Kubernetes service
* Support for Data Guard on Exadata Cloud at Customer VM clusters in the Database service
* Support for stopping VM instances after scheduled maintenance or hypervisor reboots in the Compute service
* Support for creating and managing private endpoints in the Data Flow service

====================
2.21.1 - 2020-08-18
====================

Added
-----
* Support for custom boot volume size and other node pool updates in the Container Engine for Kubernetes service
* Support for Data Guard on Exadata Cloud at Customer VM clusters in the Database service
* Support for stopping VM instances after scheduled maintenance or hypervisor reboots in the Compute service
* Support for creating and managing private endpoints in the Data Flow service

====================
2.21.0 - 2020-08-11
====================

Added
-----
* Support for autonomous json databases in the Database service
* Support for cleaning up uncommitted multipart uploads in the Object Storage service
* Support for additional list API filters in the Data Catalog service

Breaking
--------
* Some unusable region enums were removed from the Support Management service
* Parameter `opc_retry_token` was removed from the Support Management service

====================
2.20.0 - 2020-08-04
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the uk-gov-cardiff-1 region
* Support for creating and managing private endpoints in the Data Flow service
* Support for changing instance shapes and restarting nodes in the Big Data service
* Support for additional versions (for example CSQL) in the Big Data service
* Support for creating stacks from compartments in the Resource Manager service

Breaking
--------
* Param `life_cycle_details` renamed to `lifecycle_details` in models `BlockchainPlatformByHostname` and `BlockchainPlatformSummary` in the Blockchain service

Changed
-------
* Restricted `pyOpenSSL` dependency to versions between 17.5.0 and 19.1.0, both inclusive. See `#255 <https://github.com/oracle/oci-python-sdk/issues/255>`_ for details.

====================
2.19.0 - 2020-07-28
====================

Added
-----
* Support for calling Oracle Cloud Infrastructure services in the us-sanjose-1 region
* Support for updating the fault domain and launch options of VM instances in the Compute service
* Support for image capability schemas and schema versions in the Compute service
* Support for 'Patch Now' maintenance runs for autonomous Exadata infrastructure and autonomous container database resources in the Database service
* Support for automatic performance and cost tuning on volumes in the Block Storage service

Breaking
--------
* Removed the accessToken field from the GitlabAccessTokenConfigurationSourceProvider model in the Resource Manager service

====================
2.18.1 - 2020-07-21
====================

Added
-----
* Support for license types on instances in the Content and Experience service

Fixed
-----
* Fixed a bug for Resource Principal authentication where RPST token was not getting refreshed correctly.

====================
2.18.0 - 2020-07-14
====================

Added
-----
* Support for the Blockchain service
* Support for failing over an autonomous database that has Data Guard enabled in the Database service
* Support for switching over an autonomous database that has Data Guard enabled in the Database service
* Support for git configuration sources in the Resource Manager service
* Support for optionally specifying a VCN id on list operations of DHCP options, subnets, security lists, route tables, internet gateways, and local peering gateways in the Networking service

Fixed
-----
* Fixed a bug where user-set timeout values were not being passed to base client from service client and remained `None`. This has been fixed in all clients except the upload manager and multipart object assembler.

Breaking
--------
* Parameter `vcn_id` changed from required to optional in methods `list_dhcp_options`, `list_local_peering_gateways`, `list_route_tables`, `list_security_lists`, `list_subnets` and `list_internet_gateways` in the virtual network client. If the VCN ID is not provided, then the list includes information of all VCNs in the specified compartment.
* For upload manager and multipart object assembler, the timeout for the object storage client is overwritten to `None` for all operations which call object storage. For this reason, the operations are NOT thread-safe, and you should provide the class with its own Object Storage client that isn't used elsewhere.

====================
2.17.2 - 2020-07-07
====================

Added
-----
* Support for registering and deregistering autonomous dedicated databases with Data Safe in the Database service
* Support for switching between non-private-endpoints and private endpoints on autonomous databases in the Database service
* Support for returning group names when listing identity provider groups in the Identity service
* Support for server-side object re-encryption in the Object Storage service
* Support for private endpoint (ingress) and public endpoint whitelisting in the Analytics Cloud service

====================
2.17.1 - 2020-06-30
====================

Added
-----
* Support for the Usage service
* Support for the VMware Provisioning service
* Support for applying one-off patches to databases in the Database service
* Support for layer-2 virtualization features on vlans in the Networking service
* Support for all AttachVolumeDetails and ParavirtualizedAttachVolumeDetails properties on instance configurations in the Compute Management service
* Support for setting HTTP header size and allowing invalid characters in HTTP request headers in the Load Balancing service
* Support for enabling/disabling HTTP logging. Please see https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/logging.html

====================
2.17.0 - 2020-06-23
====================

Added
-----
* Support for the Data Integration service
* Support for updating database home IDs on databases in the Database service
* Support for backing up autonomous databases on Cloud at Customer in the Database service
* Support for managing autonomous VM clusters on Cloud at Customer in the Database service
* Support for accessing data assets via private endpoints in the Data Catalog service
* Support for dependency archive zip files to be specified for use by applications in the Data Flow service

Breaking
--------
* Attribute `lifecycle_state` in the Data Catalog service has restricted values to "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"
* Attribute `workflow_status` in the Data Catalog service has restricted values to "NEW", "APPROVED", "UNDER_REVIEW", "ESCALATED"
* Attribute `schedule_type` in the Data Catalog service has restricted values to "SCHEDULED", "IMMEDIATE"
* Attribute `job_type` in the Data Catalog service has restricted values to "HARVEST", "PROFILING", "SAMPLING", "PREVIEW", "IMPORT", "EXPORT", "INTERNAL", "PURGE", "IMMEDIATE", "SCHEDULED", "IMMEDIATE_EXECUTION", "SCHEDULED_EXECUTION", "SCHEDULED_EXECUTION_INSTANCE"
* Attribute `harvest_status` in the Data Catalog service has restricted values to "COMPLETE", "ERROR", "IN_PROGRESS", "DEFERRED"

====================
2.16.1 - 2020-06-16
====================

Added
-----
* Support for creating a new database from an existing database based on a given timestamp in the Database service
* Support for enabling archive log backups of databases in the Database service
* Support for returning the database version on autonomous container databases in the Database service
* Support for the new DNS format of the Data Transfer service
* Support for scheduled autoscaling, which allows for scaling actions triggered at particular times based on CRON expressions, in the Compute Autoscaling service
* Support for filtering of list APIs for groups, identity providers, identity provider groups, compartments, dynamic groups, network sources, policies, and users by name or lifecycle state in the Identity Service

====================
2.16.0 - 2020-06-09
====================

Added
-----
* Support for returning the database version of backups in the Database service
* Support for patching on Exadata Cloud at Customer resources in the Database service
* Support for new lifecycle substates on instances in the Digital Assistant service
* Support for file servers in the Integration service
* Support for deleting non-empty tag namespaces and bulk deleting tags in the Identity service
* Support for bulk move and bulk delete of resources by compartment in the Identity service

Breaking
--------
* Data type for parameter `data_storage_size_in_tbs` changed from int to float in the Database service
* Parameter `lifecycle_state` removed state `OFFLINE` and added `DISCONNECTED` in the Database service

====================
2.15.0 - 2020-06-02
====================

Added
-----
* Support for optionally supplying a signature when deleting an agreement in the Marketplace service
* Support for launching paid listings in non-US regions in the Marketplace service
* Support for returning the image id of packages in the Marketplace service
* Support for calling Oracle Cloud Infrastructure services in the ap-chuncheon-1 region
* Support for authenticating via Resource Principals. An example of how to use resource principals is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/resource_principals_example.py>`__

Fixed
-----
* Fixed a bug where `oci.waiter.wait_until()` was not invoking `wait_callback` correctly based on the resource property
* Fixed a bug in `ExponentialBackoffWithFullJitterRetryStrategy.do_sleep()` where it was assuming time in milliseconds but it should be seconds

Breaking
--------
* Field `signature` in `delete_accepted_agreement_id` from Marketplace Service changed from required to optional

====================
2.14.3 - 2020-05-19
====================

Added
-----
* Support for returning the private IP of a private endpoint database in the Database service
* Support for native JWT validation in the API Gateway service

====================
2.14.2 - 2020-05-12
====================

Added
-----
* Support for drift detection in the Resource Manager service

====================
2.14.1 - 2020-05-05
====================

Added
-----
* Support for updating the license type of database systems in the Database service
* Support for updating the version of 19c autonomous databases in the Database service
* Support for backup and restore functionality in the Key Management service
* Support for reports in the Marketplace service
* Support for calling Oracle Cloud Infrastructure services in the ap-hyderabad-1 region
====================
2.14.0 - 2020-04-28
====================

Added
-----
* Support for the MySQL Database service
* Support for updating the database home of a database in the Database service
* Support for government regions in the Marketplace service
* Support for starting and stopping instances in the Integration service
* Support for installing Windows updates in the OS Management service

Breaking
--------
* Deleted models ErrataId, ManagedInstanceUpdateDetails and UpdatablePackageSummary from the os_management service

====================
2.13.0 - 2020-04-21
====================

Added
-----
* Support for the Data Safe service
* Support for the Incident Management service
* Support for showing which database versions support always-free in the Database service
* Support in instance configurations for flex shapes, dedicated VM hosts, encryption in transit, and KMS keys in the Compute Autoscaling service
* Support for server-side object encryption using a customer-provided encryption key in the Object Storage service
* Support for specifying maintenance preferences while launching and updating Exadata Database systems in the Database service
* Support for flexible-shaped VM instances in the Compute service
* Support for scheduled cross-region backups in the Block Volume service
* Support for object versioning in the Object Storage service

Breaking
--------
* Deleted models Archiver, CreateArchiverDetails and UpdateArchiverDetails from the streaming service

====================
2.12.4 - 2020-04-14
====================

Added
-----
* Support for access types on instances in the Content and Experience service
* Support for identity contexts in the Search service
* Support for Client Side Encryption: https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/clientsideencryption.htm
* Support for retries on Python built-in `ConnectionError <https://docs.python.org/3/library/exceptions.html#ConnectionError>`__

====================
2.12.3 - 2020-04-07
====================

Added
-----
* Support for changing compartments of runs and applications in the Data Flow service
* Support for getting usage information in the Key Management Vault service
* Support for custom Key Management service endpoints and private endpoints on stream pools in the Streaming service
* Fixed kms_example and added secrets examples

====================
2.12.2 - 2020-03-31
====================

Added
-----
* Support for the Secrets Management service
* Support for the Big Data service
* Support for updating class name, file URI, language, and spark version of applications in the Data Flow service
* Support for cross-region replication in the Object Storage service
* Support for retention rules in the Object Storage service
* Support for enabling and disabling pod security policy admission controllers in the Container Engine for Kubernetes service

====================
2.12.1 - 2020-03-24
====================

Added
-----
* Support for Web Application Acceleration and Security configurations on instances in the Content and Experience service
* Support for shared database homes on Exadata Cloud at Customer resources in the Database service
* Support for Exadata database creation from backup in the Database service
* Support for conditions on JavaScript challenges, new action types on access rules, new policy configuration settings, exclusions on custom protection rules, and IP address lists on IP whitelists in the Web Application Acceleration and Security service

====================
2.12.0 - 2020-03-17
====================

Added
-----
* Support for serial console connections in the Database service
* Support for preview database versions in the Database service
* Support for node reboot migration maintenance status and maintenance windows in the Database service
* Support for using instance metadata API v2 for instance principals authentication
* Upgraded configparser dependency version

Breaking
--------
* Deleted model autonomous_exadata_infrastructure_maintenance_window.py from the database service

====================
2.11.0 - 2020-03-10
====================

Added
-----
* Support for Events service integration with alerts in the Budgets service

Breaking
--------
* The parameters sort_by and lifecycle_state type from Budget service are changed from str to enum

====================
2.10.7 - 2020-03-03
====================

Added
-----
* Support for updating the shape of a Database System in the Database service
* Support for generating CPE configurations for download in the Networking service
* Support for private IPs and fault domains of cluster nodes in the Container Engine for Kubernetes service
* Support for calling Oracle Cloud Infrastructure services in the ca-montreal-1 region
* Fixed missed parameter when invoking request signing for delegation token

====================
2.10.6 - 2020-02-25
====================

Added
-----
* Support for restarting autonomous databases in the Database service
* Support for private endpoints on autonomous databases in the Database service
* Support for IP-based policies in the Identity service
* Support for management of OAuth 2.0 client credentials in the Identity service
* Support for OCI Functions as a subscription protocol in the Notifications service

====================
2.10.5 - 2020-02-18
====================

Added
-----
* Support for the NoSQL Database service
* Support for filtering database versions by storage management type in the Database service
* Support for specifying paid listing types within pricing models in the Marketplace service
* Support for primary and non-primary instance types in the Content and Experience service

====================
2.10.4 - 2020-02-11
====================

Added
-----
* Support for listing supported database versions for Autonomous Database Serverless, and selecting a version at provisioning time in the Database service
* Support for TCP proxy protocol versions on listener connection configurations in the Load Balancer service
* Support for calling the Notifications service in alternate realms
* Support for calling Oracle Cloud Infrastructure services in the eu-amsterdam-1 and me-jeddah-1 regions

====================
2.10.3 - 2020-02-04
====================

Added
-----
* Support for the Data Science service
* Support for calling Oracle Cloud Infrastructure services in the ap-osaka-1 and ap-melbourne-1 regions

====================
2.10.2 - 2020-01-28
====================

Added
-----
* Support for the Application Migration service
* Support for the Data Flow service
* Support for the Data Catalog service
* Support for cross-shape Data Guard in the Database service
* Support for offline data export in the Data Transfer service

====================
2.10.1 - 2020-01-21
====================

Added
-----
* Support for getting DRG redundancy status in the Networking service
* Support for cloning autonomous databases from backups in the Database service

====================
2.10.0 - 2020-01-14
====================

Added
-----
* Support for a description field on route rules and security rules in the Networking service
* Support for starting and stopping Digital Assistant instances in the Digital Assistant service
* Support for shared database homes on Exadata, bare metal, and virtual machine instances in the Database service
* Support for tracking a number of Database service operations through the Work Requests service

Breaking
--------
* Field `db_home_id` in `list_databases` from database service is changed from required to optional

====================
2.9.0 - 2020-01-07
====================

Added
-----
* Support for optionally specifying the corporate proxy field when creating Exadata infrastructure in the Database service
* Support for maintenance windows, and rescheduling maintenance runs, on autonomous container databases in the Database service
* Provide example on how to use key_content for python SDK configuration

Breaking
--------
* Field `host_name` in `NodeDetails` from database service is changed from optional to required

====================
2.8.0 - 2019-12-17
====================

Added
-----
* Support for the API Gateway service
* Support for the OS Management service
* Support for the Marketplace service
* Support for "default"-type vaults in the Key Management service
* Support for bringing your own keys in the Key Management service
* Support for cross-region backups of boot volumes in the Block Storage service
* Support for top-level TSIG keys in the DNS service
* Support for resizing virtual machine instances to different shapes in the Compute service
* Support for management configuration of cloud agents in the Compute service
* Support for launching node pools using image IDs in the Container Engine for Kubernetes service

Breaking
--------
* Removed support for v1 auth tokens in kubeconfig files in the `CreateClusterKubeconfigContentDetails` class of the Container Engine for Kubernetes service
* Removed the IDCS access token requirement on the delete deleteOceInstance operation in the Content and Experience service, which is why the `DeleteOceInstanceDetails` class was removed
* Set `compartment_id` as a required parameter in `list_stream_pools` for streaming service

====================
2.7.1 - 2019-12-10
====================

Added
-----
* Support for etags on results of the List Objects API in the Object Storage service
* Support for OCIDs on buckets in the Object Storage service
* Support for content-disposition and cache-control headers on objects in the Object Storage service
* Support for recovering deleted compartments in the Identity service
* Support for sharing volumes across multiple instances in the Block Storage service
* Support for connect harnesses and stream pools in the Streaming service
* Support for associating file storage mount targets with network security groups in the File Storage service
* Support for calling Oracle Cloud Infrastructure services in the uk-gov-london-1 region
* Add default connection timeout(10s) and read timeout(60s) for Python SDK client
* Add contents table to client documentation
* Fix the issue of the second style of pagination

====================
2.7.0 - 2019-11-26
====================

Added
-----
* Support for maintenance windows on autonomous databases in the Database service
* Support for getting the compute units (OCPUs) of an Exadata autonomous transaction processing - dedicated resource in the Database service

Breaking changes
----
* Create database home from VM_CLUSTER_BACKUP is removed from Database Service

====================
2.6.5 - 2019-11-19
====================

Added
-----
* Support for four-byte autonomous system numbers (ASNs) on FastConnect resources in the Networking service
* Support for choosing fault domains when creating instance pools in the Compute service
* Support for allowing connections from only specific VCNs to autonomous data warehouse and autonomous transaction processing instances in the Database service
* Support for Streaming Client Non-Regional

====================
2.6.4 - 2019-11-12
====================

Added
-----
* Support for access to APEX and SQL Dev features on autonomous transaction processing and autonomous data warehouse resources in the Database service
* Support for registering / deregistering autonomous transaction processing and autonomous data warehouse resources with Data Safe in the Database service
* Support for redirecting HTTP / HTTPS request URIs to different URIs in the Load Balancing service
* Support for specifying compartments on options APIs in the Container Engine for Kubernetes service
* Support for volume performance units on block volumes in the Block Storage service

====================
2.6.3 - 2019-11-05
====================

Added
-----
* Support for the Analytics Cloud service
* Support for the Integration Cloud service
* Support for IKE versions in IPSec connections in the Virtual Networking service
* Support for getting a stack's Terraform state in the Resource Manager service

====================
2.6.2 - 2019-10-29
====================

Added
-----
* Support for wallet rotation operations on Autonomous Databases in the Database service
* Support for adding and removing image shape compatibility entries in the Compute service
* Support for managing redirects in the Web Application Acceleration and Security service
* Support for migrating zones from the Dyn HTTP Redirect Service to Oracle Cloud Infrastructure in the DNS service

====================
2.6.1 - 2019-10-15
====================

Added
-----
* Support for the Digital Assistant service
* Support for work requests on Instance Pool operations in the Compute service

====================
2.6.0 - 2019-10-08
====================

Added
-----
* Support for the new schema for events in the Audit service
* Support for entitlements in the Data Transfer service
* Support for custom scheduled backup policies on volumes in the Block Storage service
* Support for specifying the network type when launching virtual machine instances in the Compute service
* Support for Monitoring service integration in the Health Checks service

Breaking
--------
* The tenant_id parameter is now id (Id of the Transfer Application Entitlement) for get_transfer_appliance_entitlement in TransferApplianceEntitlementClient
* The topic_attributes_details parameter is now required for update_topic in NotificationControlPlaneClient
* The Audit service version was bumped to 20190901, use older version of Python SDK for Audit service version 20160918

====================
2.5.2 - 2019-10-01
====================

Added
-----
* Support for required tags in the Identity service
* Support for work requests on tagging operations in the Identity service
* Support for enumerated tag values in the Identity service
* Support for moving dynamic routing gateway resources across compartments in the Networking service
* Support for migrating zones from Dyn managed DNS to OCI in the DNS service
* Support for fast provisioning for virtual machine databases in the Database service

====================
2.5.1 - 2019-09-24
====================

Added
-----
* Support for selecting the Terraform version to use in the Resource Manager service
* Support for bucket re-encryption in the Object Storage service
* Support for enabling / disabling bucket-level events in the Object Storage service

====================
2.5.0 - 2019-09-17
====================

Added
-----
* Support for importing state files in the Resource Manager service
* Support for Exadata Cloud at Customer in the Database service
* Support for free tier resources and system tags in the Load Balancing service
* Support for free tier resources and system tags in the Compute service
* Support for free tier resources and system tags in the Block Storage service
* Support for free tier and system tags on autonomous databases in the Database service

Breaking
--------
* The availability_domain parameter is now a kwarg for list_db_system_shapes in DatabaseClient
* The model CreateDbHomeWithDbSystemIdBase was renamed CreateDbHomeBase and the parameter db_system_id was removed
* The parameter create_db_home_with_db_system_id_details for create_db_home in DatabaseClient changed from CreateDbHomeWithDbSystemIdBase to CreateDbHomeBase

====================
2.4.0 - 2019-09-10
====================

Added
-----
* Support for specifying the autoBackupWindow field for scheduling backups in the Database service
* Support for network security groups on autonomous Exadata infrastructure in the Database service
* Support for Kubernetes secrets encryption in customer clusters, regional subnets, and cluster authentication for instance principals in the Container Engine for Kubernetes service
* Support for the Oracle Content and Experience service

Breaking
--------
* The etag header has been removed from the response for NotificationControlPlaneClient.change_topic_compartment and NotificationDataPlaneClient.change_subscription_compartment

====================
2.3.3 - 2019-09-03
====================

Added
-----
* Support for the Sydney (SYD) region
* Support for managing cluster networks in the Compute Autoscaling service
* Support for tracking asynchronous operations via work requests in the Database service

====================
2.3.2 - 2019-08-27
====================

Added
-----
* Support for the Sao Paulo (GRU) region
* Support for dedicated virtual machine hosts in the Compute service
* Support for resource groups in metrics and alarms in the Monitoring service

====================
2.3.1 - 2019-08-20
====================

Added
-----
* Support for the Limits service
* Support for archiving to Object Storage in the Streaming service
* Support for etags on resources in the Streaming service
* Support for Key Management service (KMS) encryption of file systems in the File Storage service
* Support for moving public IP, DHCP, local peering gateway, internet gateway, network security group, and DRG attachment resources across compartments in the Networking service
* Support for multi-origin, basic cache, certificate mapping, and OCI Monitoring service integration in the Web Application Acceleration and Security service

====================
2.3.0 - 2019-08-13
====================

Added
-----
* Support for the Data Transfer service
* Support for the Zurich (ZRH) region

Breaking
--------
* oci.waas.WafLog.timestamp type changed from str to datetime
* oci.waas.models.Certificate.issuer_name type changed from oci.waas.models.CertificateSubjectName to oci.waas.models.CertificateIssuerName
* `"PURGE_WAAS_POLICY"` removed as option for oci.waas.models.WorkRequest.operation_type
* `"PURGE_WAAS_POLICY"` removed as option for oci.waas.models.WorkRequestSummary.operation_type

====================
2.2.21 - 2019-08-06
====================

Added
-----
* Support for IPv6 load balancers in the Load Balancing service
* Support for IPv6 on VCN and FastConnect resources in the Networking service

====================
2.2.20 - 2019-07-30
====================

Added
-----
* Support for the Mumbai (BOM) region
* Support for the Events service
* Support for moving streams across compartments in the Streaming service
* Support for moving FastConnect resources across compartments in the Networking service
* Support for moving policies across compartments in the Web Application Acceleration and Security service
* Support for tagging FastConnect resources in the Networking service

====================
2.2.19 - 2019-07-23
====================

Added
-----
* Support for moving resources across compartments in the Database service
* Support for moving resources across compartments in the Health Checks service
* Support for moving alarms across compartments in the Monitoring service
* Support for creating instance configurations from running instances in the Compute service
* Support for setting up budget alerts for cost tracking tags in the Budgets service

====================
2.2.18 - 2019-07-16
====================

Added
-----
* Support for the Functions service
* Support for the Quotas service
* Support for moving resources across compartments in the DNS service
* Support for moving instances across compartments in the Compute service
* Support for moving keys and vaults across compartments in the Key Management service
* Support for moving topics and subscriptions across compartments in the Notifications service
* Support for moving load balancers across compartments in the Load Balancing service
* Support for specifying permitted REST methods in load balancer rule sets in the Load Balancing service
* Support for configuring cookie session persistence in backend sets in the Load Balancing service
* Support for ACL rules in rule sets in the Load Balancing service
* Support for move compartment tree in the Identity service
* Support for specifying and returning a KMS key in backup operations in the Block Storage service
* Support for transit routing in the Networking service
* Support for authenticating via Resource Principals. An example of how to use resource principals is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/resource_principals_example.py>`__. This authentication method is only supported within the Functions service at this time.

====================
2.2.17 - 2019-07-09
====================

Added
-----
* Support for network security groups in the Load Balancing service
* Support for network security groups in Core Services
* Support for network security groups on database systems in the Database service
* Support for creating autonomous transaction processing and autonomous data warehouse previews in the Database service
* Support for getting the load balancer attachments of instance pools in the Compute service
* Support for moving resources across compartments in the Resource Manager service
* Support for moving VCN resources across compartments in the Networking service

====================
2.2.16 - 2019-07-02
====================

Added
-----
* Support for moving images, instance configurations, and instance pools across compartments in Core Services
* Support for moving autoscaling configurations across compartments in the Compute Autoscaling service

Fixed
-----
* Fixed a bug where the Streaming service's endpoints in Tokyo, Seoul, and future regions were not reachable from the SDK

====================
2.2.15 - 2019-06-25
====================

Added
-----
* Support for moving senders across compartments in the Email service
* Support for moving NAT gateway resources across compartments in Core Services

====================
2.2.14 - 2019-06-18
====================

Added
-----
* Support for moving service gateway resources across compartments in Core Services
* Support for moving block storage resources across compartments in Core Services
* Support for key deletion in the Key Management service

====================
2.2.13 - 2019-06-11
====================

Added
-----
* Support for specifying custom boot volume sizes on instance configurations in the Compute Autoscaling service
* Support for 'Autonomous Transaction Processing - Dedicated' features, as well as maintenance run and backup operations on autonomous databases, autonomous container databases, and autonomous Exadata infrastructure in the Database service

====================
2.2.12 - 2019-06-04
====================

Added
-----
* Support for autoscaling autonomous databases and autonomous data warehouses in the Database service
* Support for specifying fault domains as part of instance configurations in the Compute Autoscaling service
* Support for deleting tag definitions and tag namespaces in the Identity service

Fixed
-----
* Support for regions in realms other than oraclecloud.com in the Load Balancing service

====================
2.2.11 - 2019-05-28
====================

Added
-----
* Support for the Work Requests service, and tracking of a number of Core Services operations through work requests
* Support for emulated volume attachments in Core Services
* Support for changing the compartment of resources in the File Storage service
* Support for tags in list operations in the File Storage service
* Support for returning UI password creation dates in the Identity service

====================
2.2.10 - 2019-05-21
====================

Added
-----
* Support for returning tags when listing instance configurations, instance pools, or autoscaling configurations in the Compute Autoscaling service
* Support for getting the namespace of another tenancy than the caller's tenancy in the Object Storage service
* Support for BGP dynamic routing and providing pre-shared secrets (PSKs) when establishing tunnels in the Networking service

====================
2.2.9 - 2019-05-14
====================

Added
-----
* Support for the Seoul (ICN) region
* Support for logging context fields on data-plane APIs of the Key Management Service
* Support for reverse pagination on list operations of the Email service
* Support for configuring backup retention windows on database backups in the Database service
* Support for subscribed regions in stop_untagged_instances.py on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/stop_untagged_instances.py>`__.
* New services to showoci.py on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/showoci/showoci.py>`__.

====================
2.2.8 - 2019-05-07
====================

Added
-----
* Support for the Tokyo (NRT) region
* A sample demonstrating how to find, stop and report on instances that have been improperly tagged is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/stop_untagged_instances.py>`__.
* A sample demonstrating adding and deleting an API key is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/add_API_key.py>`__.
* New services to showoci.py on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/showoci/showoci.py>`__.

Fixed
-----
* Updated example for Streaming service to address issue with encoding in Python 3 is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/stream_example.py>`__.

====================
2.2.7 - 2019-04-16
====================

Added
-----
* Support for tagging dynamic groups in the Identity service
* Support for updating network ACLs and license types for autonomous databases and autonomous data warehouses in the Database service
* Support for editing static routes and IPSec remote IDs in the Virtual Networking service
* An example for reporting details for multiple Oracle Cloud Infrastructure resources is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/showoci/showoci.py>`__.

====================
2.2.6 - 2019-04-09
====================

Added
-----
* Support for etag and if-match headers (for optimistic concurrency control) in the Email service

====================
2.2.5 - 2019-04-02
====================

Added
-----
* Support for provider service key names on virtual circuits in the FastConnect service
* Support for customer reference names on cross connects and cross connect groups in the FastConnect service
* A sample showing how to use Streaming service from the SDK is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/stream_example.py>`__.

====================
2.2.4 - 2019-03-26
====================

Added
-----
* Support for glob patterns and exclusions for object lifecycle management in the Object Storage service
* Documentation enhancements and corrections for traffic management in the DNS service

====================
2.2.3 - 2019-03-19
====================

Added
-----
* Support for specifying metadata on node pools in the Container Engine for Kubernetes service
* Support for provisioning a new autonomous database or autonomous data warehouse as a clone of another in the Database service

Changed
-------
* Updated vendored packages. idna==2.8, PyJWT==1.7.1, requests==2.21.0, six==1.12.0, urllib3==1.24.1, requests==2.21.0

====================
2.2.2 - 2019-03-12
====================

Added
-----
* Support for the Budgets service
* Support for managing multifactor authentication in the Identity service
* Support for managing default tags in the Identity service
* Support for account recovery in the Identity service
* Support for authentication policies in the Identity service
* Support for specifying the workload type when creating autonomous databases in the Database service
* Support for I/O resource management for Exadata database systems in the Database service
* Support for customer-specified timezones on database systems in the Database service

====================
2.2.1 - 2019-02-28
====================

Added
-----
* Support for the Monitoring service
* Support for the Notification service
* Support for the Resource Manager service
* Support for the Compute Autoscaling service
* Support for changing the compartment of a tag namespace in the Identity service
* Support for specifying fault domains in the Database service
* Support for managing instance monitoring in the Compute service
* Support for attaching/detaching load balancers to instance pools in the Compute service

====================
2.2.0 - 2019-02-21
====================

Added
-----
* Support for government-realm regions
* Support for the Streaming service
* Support for tags in the Key Management service
* Support for regional subnets in the Virtual Networking service

Fixed
-----
* Removed unused Announcements service 'NotificationFollowupDetails' model and 'followups' from Announcement model

====================
2.1.7 - 2019-02-07
====================

Added
-----
* Support for the Web Application Acceleration and Security (WAAS) service
* Support for the Health Checks service
* Support for connection strings on Database resources in the Database service
* Support for traffic management in the DNS service
* Support for tagging in the Email service

====================
2.1.6 - 2019-01-31
====================

Added
-----
* Support for the Announcements service

====================
2.1.5 - 2019-01-24
====================

Added
-----
* Support for renaming databases during restore-from-backup operations in the Database service
* Support for calling Oracle Cloud Infrastructure services in the ca-toronto-1 region

Fixed
-----
* KmsCryptoClient and KmsManagementClient updated to make service_endpoint required
* Explicitly imported path to idna. Addresses `GitHub issue 101 <https://github.com/oracle/oci-python-sdk/issues/101>`__

====================
2.1.4 - 2019-01-10
====================

Added
-----
* Support for device attributes on volume attachments in the Compute service
* Support for custom header rulesets in the Load Balancing service

====================
2.1.3 - 2018-12-13
====================

Added
-----
* Support for Data Guard for VM shapes in the Database service
* Support for sparse disk groups for Exadata shapes in the Database service
* Support for a new field, isLatestForMajorVersion, when listing DB versions in the Database service
* Support for in-transit encryption for paravirtualized boot volume and data volume attachments in the Block Storage service
* Support for tagging DNS Zones in the DNS service
* Support for resetting credentials for SCIM clients associated with an Identity provider and updating user capabilities in the Identity service

Security
-------
* pyOpenSSL pinning was changed to pyOpenSSL>=17.5.0 and cryptography pinning to cryptography>=2.1.4 to address vulnerability `CVE-2018-1000808 <https://nvd.nist.gov/vuln/detail/CVE-2018-1000808>`__

====================
2.1.2 - 2018-11-29
====================

Added
-----
* Support for getting bucket statistics in the Object Storage service
* Support for using FIPS compliant libcrypto library

Fixed
-----
* Block Storage service for copying volume backups across regions is now enabled

====================
2.1.1 - 2018-11-15
====================

Added
-----
* Support for VCN transit routing in the Networking service

Fixed
-----
* Fixed UploadManager to work with unbuffered streams in Python 3

====================
2.1.0 - 2018-11-01
====================

Added
-----
* Support for modifying the route table, DHCP options and security lists associated with a subnet in the Networking service.
* Support for tagging of File Systems, Mount Targets and Snapshots in the File Storage service.
* Support for nested compartments in the Identity service

Breaking
--------
* database_size_in_g_bs field in Backup and BackupSummary models renamed to database_size_in_gbs.

====================
2.0.6 - 2018-10-18
====================

Added
-----
* Support for cost tracking tags in the Identity service
* Support for generating and downloading wallets in the Database service
* Support for creating a standalone backup from an on-premises database in the Database service
* Support for db version and additional connection strings in the Autonomous Transaction Processing and Autonomous Data Warehouse resources of the Database service
* Support for copying volume backups across regions in the Block Storage service
* Support for deleting compartments in the Identity service
* Support for reboot migration for virtual machines in the Compute service
* Support for Instance Pools and Instance Configurations in the Compute service

Changed
-------
* database_edition field in Backup and model changed from a free format string to a validated string. It will only accept one of the following: “STANDARD_EDITION”, “ENTERPRISE_EDITION”, “ENTERPRISE_EDITION_HIGH_PERFORMANCE”, “ENTERPRISE_EDITION_EXTREME_PERFORMANCE”

Breaking
--------
* db_data_size_in_mbs field in Backup and BackupSummary models renamed to database_size_in_g_bs. The type changed from int to float.

====================
2.0.5 - 2018-10-04
====================

Added
-----
* Support for trusted partner images through application listings and subscriptions in the Compute service
* Support for object lifecycle policies in the Object Storage service
* Support for copying objects across regions in the Object Storage service
* Support for network address translation (NAT) gateways in the Networking service

====================
2.0.4 - 2018-09-27
====================

Added
-----
* Support for paravirtualized launch mode when importing images in the Compute service
* Support for Key Management service
* Support for encrypting the contents of an Object Storage bucket using a Key Management service key
* Support for specifying a Key Management service key when launching a compute instance in the Compute service
* Support for specifying a Key Management service key when backing up or restoring a block storage volume in the Block Volume service

Fixed
-----
* ObjectStorageClient requires int value for content_length keyword argument to put_object and upload_part, but the SDK was not converting the type for the Requests library.

====================
2.0.3 - 2018-09-06
====================

Added
-----
* Added support for updating metadata fields on an instance in the Compute service

Fixed
-----
* Fixed example wait_for_resource_in_state.py to use existing response objects.  The updated example can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/wait_for_resource_in_state.py>`__.

====================
2.0.2 - 2018-08-23
====================

Added
-----
* Support for fault domains in the Identity service
* Support for resizing an offline volume in the Block Storage service
* Support for Autonomous Data Warehouse and Autonomous Transaction Processing in the Database service

Changed
-------
* Opened up the dependency pinning on cryptography due to `CVE-2018-10903 <https://nvd.nist.gov/vuln/detail/CVE-2018-10903>`__.  OCI does not call the affected method in cryptography, but upgrading is recommended.

====================
2.0.1 - 2018-08-09
====================

Added
-----
* Support for fault domains in the Compute service
* A sample showing how to use Search service from the SDK is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/search_example.py>`__.

====================
2.0.0 - 2018-07-26
====================

Added
-----
* Support for the OCI Search service
* Support for specifying a backup policy when creating a boot volume in the Block Storage service
* Added retries to the InstancePrincipalsSecurityTokenSigner when trying to refresh security tokens

Changed
-------
* Add six, requests, urllib3, idna, and chardet as vendored packages.

Fixed
-----
* Downloading an object from Object Storage could fail without an exception if the connection was closed while the object was being transmitted.

Breaking
--------
* The base exception from requests, `requests.exceptions.RequestException`, has been wrapped in oci.exceptions.RequestExceptions
* `requests.exceptions.ConnectTimeout` has been wrapped in oci.exceptions.ConnectTimeout

====================
1.4.5 - 2018-07-12
====================

Added
-----
* Support for tagging Load Balancers in the Load Balancing service
* Support for export options in the File Storage service
* Support for retrieving compartment name and user name as part of events in the Audit service

Changed
-------
* Setup.py updated to allow more version of cryptography when installing to an existing environment
* Add PyJWT as a vendored package


====================
1.4.4 - 2018-06-28
====================

Added
-----
* Support for service gateway management in the Networking service
* Support for backup and clone of boot volumes in the Block Storage service

Changed
-------
* Setup.py changed to allow more versions of pytz and python-dateutil packages when installing to an existing environment

====================
1.4.3 - 2018-06-14
====================

Added
-----
* Support for the Container Engine service

  * A sample showing how to use this service from the SDK is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/container_engine.py>`__.

Fixed
-------
* Add dependency to idna >=2.5,<2.7 since cryptography and requests both have a dependency on the library and pip can install a version that is incompatible with requests.

====================
1.4.2 - 2018-06-14
====================

This version was removed from PyPi due to a potential dependency conflict between cryptography and requests.

* Support for the Container Engine service

  * A sample showing how to use this service from the SDK is available on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/container_engine.py>`__.

====================
1.4.1 - 2018-05-31
====================

Added
-----
* Support for the "soft shutdown" instance action in the Compute service
* Support for Auth Token management in the Identity service

Changed
-------
* Bumped required version of python-dateutil to 2.7.3

====================
1.4.0 - 2018-05-17
====================

Added
-----
* Support for launching a database system from a backup in the Database service
* Support for backup or clone of multiple volumes at once using volume groups in the Block Storage service
* Support for tagging virtual cloud network resources in the Networking service
* Support for specifying the PARAVIRTUALIZED remote volume type when creating a virtual image or launching a new instance in the Compute service
* Example to retrieve network information for an instance which can be found on `Github <https://github.com/oracle/oci-python-sdk/blob/master/examples/get_all_instance_ip_addresses_and_dns_info.py>`__.

Changed
-------
* Added retrieving and setting the home region to the user_crud.py example which can be found on `Github <https://github.com/oracle/oci-python-sdk/blob/master/examples/user_crud.py>`__.

Breaking
--------
* In ``FileStorageClient.list_exports`` the ``compartment_id`` parameter has moved from a positional to a keyword argument.  This requires a code change as a v1.3.x call would look like: ``file_storage_client.list_exports('ocid1....')`` but in v1.4.x+ it would look like ``file_storage_client.list_exports(compartment_id='ocid1....')``

====================
1.3.20 - 2018-05-03
====================

Added
-----
* Support for returning names for events in the Audit service
* Support for multiple hostnames per listener in the Load Balancing service
* Helper function for Base64-ing scripts for user_data in launch instance options

  * An example of Base64-ing scripts for user_data can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/launch_instance_example.py>`__.

Changed
-------
* Add httpsig_cffi as a vendored package

Fixed
-----
* Multipart object put resume to account when final part is less than part size

====================
1.3.19 - 2018-04-19
====================

Added
-----
* Support for tagging ``DbSystem`` and ``Database`` resources in the Database Service
* Support for filtering by ``DbSystemId`` in ``ListDbVersions`` operation in Database Service
* Support for composite operations that provide convenience methods for operations that can be chained together (e.g. launching an instance and waiting for it to enter the RUNNING state)

  * An example on how to perform these operations can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/composite_operations_example.py>`__.


====================
1.3.18 - 2018-04-05
====================

Added
-----
* Added Python 3.6 as a supported Python version

Fixed
------
* Python API reference documentation improvements


====================
1.3.17 - 2018-03-26
====================

Added
------
* Added support for remote VCN peering across regions

  * An example on how to perform these operations can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/remote_peering_connection_example.py>`__.

* Added support for calling Oracle Cloud Infrastructure services in the uk-london-1 (LHR) region


====================
1.3.16 - 2018-03-08
====================

Added
-----
* Added support for the Email Service

  * An example on using the Email Service can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/email_service_example.py>`__.

* Added support for SMTP credentials in the Identity Service

  * An example on managing SMTP credentials can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/email_service_example.py>`__.

* Added support for paravirtualized volume attachments in Core Services

  * An example on using volume attachments can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/volume_attachment_example.py>`__.

* Added support for variable size boot volumes in Core Services

====================
1.3.15 - 2018-02-22
====================

Added
-----
* Support for File Storage Service

  * An example on using the File Storage Service can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/file_storage_example.py>`__.

* Added support for tagging Bucket resources in the Object Storage Service

  * An example on tagging buckets can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/object_storage_bucket_tagging_example.py>`__.

* Added support  for specifying a restore period for archived objects in the ``RestoreObjects`` operation of the Object Storage service.

  * An example on using archive storage can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/object_storage_archive_example.py>`__.

====================
1.3.14 - 2018-02-08
====================

Added
-----
* Support for Domain Name System Service

  * An example on using the Domain Name System Service can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/dns_service_example.py>`_.

* Support for reserved public IPs in Virtual Networking Service

  * An example on using this functionality can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/reserved_public_ip_example.py>`_.

* Support for path route sets in Load Balancing Service

  * An example on using this functionality can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/load_balancer_path_route_sets_example.py>`_.

* Support for automated and policy-based backups, read-only volume attachments, and incremental backups in Block Storage Service

  * An example on using policy-based backups can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/volume_backup_policy_example.py>`_.

* Support for filtering by ``backupId`` in ``ListDbSystems`` operation in Database Service

====================
1.3.13 - 2018-01-25
====================

Added
-----
* Support for using the ``ObjectReadWithoutList`` public access type when creating and updating buckets
* Support for dynamic groups in Identity Service
* Support for instance principals authentication when calling OCI services. An example of how to use instance principals authentication can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/instance_principals_examples.py>`_.
* Support for configuring idle timeout for listeners in Load Balancer Service
* Support for VNC console connections in Compute Service

====================
1.3.12 - 2018-01-11
====================

Added
-----
* Support for tagging:

  * Support for creating, updating, retrieving and listing tags and tag namespaces (these operations can be found in Identity Service)
  * Support for adding freeform and defined tags to resources in Core Services (Networking, Compute, and Block Volume) and Identity Service
  * An example on using tagging can be found on `GitHub <https://github.com/oracle/oci-python-sdk/blob/master/examples/tagging.py>`_.

* Support for bringing your own custom image for emulation mode virtual machines in Compute Service
* Added the ``oci.pagination`` module, which contains convenience functions so that you don't have to manually deal with page tokens when using list operations. See the `documentation <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/pagination.html>`_ for more information

Changed
-------
* Upgraded cryptography dependency to 2.1.3

  * Added dependency on pyOpenSSL <= 17.4.0 as the minimum cryptography version for pyOpenSSL 17.5.0 is 2.1.4

* Upgraded six dependency to 1.11.0
* Upgraded requests dependency to 2.18.4

====================
1.3.11 - 2017-12-11
====================

Added
-----
* Support for public peering for FastConnect
* Support for specifying an authorized entity name in a Letter of Authority
* Support for showing a list of bandwidth shapes for a specific provider (the ``list_fast_connect_provider_virtual_circuit_bandwidth_shapes`` in ``VirtualNetworkClient``)

Changed
-------
* Audit events now have a ``response_payload`` attribute which contains metadata of interest. For example, the OCID of a resource

Deprecated
-----------
* The ``list_virtual_circuit_bandwidth_shapes`` operation in ``VirtualNetworkClient`` has been deprecated. Use the ``list_fast_connect_provider_virtual_circuit_bandwidth_shapes`` operation instead
* When using ``CreateVirtualCircuitDetails``, supplying a ``provider_name`` is deprecated and ``provider_service_id`` should be used instead

====================
1.3.10 - 2017-11-27
====================

Added
-----
* Support for initializing model objects from keyword arguments
* Support for VCN to VCN peering within the same region
* Support for sorting and filtering in list APIs in Load Balancing service
* Support for user managed boot volumes
* Support for using a second physical NIC when attaching VNICs on X7 Bare Metal instances

Fixed
-----
* Model types now check the data types of their attributes prior to data being serialized and sent to the service
* When opc_request_id is specified as a parameter, it is no longer overwritten with a SDK-generated value

====================
1.3.9 - 2017-11-02
====================

Added
-----
* Support for the Audit service
* Support for archive storage tier, object rename and namespace metadata in Object Storage service
* Support for fast clones of volumes in Block Storage service
* Support for backup and restore in Database service
* Support for sorting and filtering in list APIs in Core Services
* Support for passing explicit None values to service operations. Consult the *Passing explicit Null/None values* section of the `docs <https://oracle-cloud-infrastructure-python-sdk.readthedocs.io>`_ for more information.
* Support for supplying private key contents through the 'key_content' config field

Changed
-------
* Upgraded cryptography dependency to 1.9.
* Minimum version of Mac OS supported is now 10.8

====================
1.3.8 - 2017-10-12
====================

Deprecated
----------
* Creating block volumes and specifying the size in MBs is deprecated. Instead, the new size_in_gbs field should be used to specify the volume size in GBs.

Added
-----
* Support for creating block volumes and specifying the size in GBs.
* Support in UploadManager for handling piped input.
* Support for adding and updating display names for captured instance serial console data.
* Support for VNIC source/destination checks.
* Support for new Database service features: VM DBs, Bring Your Own License, and Data Guard.
* Support for the FRA (eu-frankfurt-1) region.

Changed
-------
* The size of block volumes and volume backups is specified in GBs as well as MBs.

====================
1.3.7 - 2017-09-11
====================

Deprecated
----------
* The top level namespace / package name has been changed from oraclebmc to oci. The oraclebmc package is deprecated and will no longer be maintained starting March 2018. Please upgrade to the oci package to avoid interruption at that time. More info is available `here <http://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/backward-compatibility.html>`_.
* The default configuration file location has been changed from ~/.oraclebmc/config to ~/.oci/config. The old location still works if the file at the new location does not exist.

Added
-----
* Support for the Database service
* Support for instance console connections
* Support for the Load Balancer Health Status API
* Support for Compartment renaming
* Support for managing customer secret keys

Changed
-------
* The default configuration file location is now ~/.oci/config

====================
1.3.6 - 2017-08-10
====================

Added
-------
* Documentation for UploadManager.

Changed
-------
* Upgraded cryptography dependency to 1.8.2.

====================
1.3.5 - 2017-07-20
====================

Added
-------
* Support for VCN multi-VNIC operations.
* Support for VCN secondary IP operations.
* Support for compute image import/export operations.

====================
 1.3.4 - 2017-06-16
====================

Fixed
-------

* Fixed bug in support for load balancing service.

====================
 1.3.3 - 2017-06-09
====================

Added
-------

* An UploadManager class to better support large object uploads through multipart and parallel operations.
* Support for object storage pre-authenticated requests and public buckets.
* Support for load balancing service.
* Support for nested instance metadata operations.

====================
 1.3.2 - 2017-05-18
====================

Added
-------

* Support for VCN private subnets using the prohibit_public_ip_on_vnic parameter on oci.core.VirtualNetworkClient.create_subnet.
* Support for FastConnect
* Support for list_regions and region subscription operations
* First class support for new IAD region

Fixed
-------

* For manually created configs (not from a file), use default values for optional fields that are not present (`GitHub issue <https://github.com/oracle/bmcs-python-sdk/issues/13>`_)
* Updated parsing of 'region' config value to enable better support for unrecognized regions

====================
 1.3.1 - 2017-04-27
====================

Changed
-------

* No longer throwing exceptions for unrecognized enum values returned by services.  Any unrecognized enum value returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.

====================
 1.3.0 - 2017-04-06
====================

Added
-------

* Support for DHCP Search Domain Option.
* Support for ComputeClient.get_windows_instance_initial_credentials.

====================
 1.2.0 - 2017-03-28
====================

Fixed
-------

* Allow service responses to deserialize to base classes when unknown subtypes are returned. Previously this would result in an exception.

Added
-------

* Support hostnames for instances and DNS labels for VCNs and subnets.

====================
 1.1.2 - 2017-03-16
====================

Changed
-------

* Updated cryptography version to 1.8.1

====================
 1.1.1 - 2017-02-23
====================

Added
-------

* Support for iPXE script parameter to launch_instance operation
* Support for stateless security list rules

====================
 1.1.0 - 2017-02-03
====================

Added
-------

* Support added for Core Services:

  * Block Storage
  * Compute
  * Virtual Network

====================
 1.0.0 - 2017-01-17
====================


Added
-------

* Initial Release
* Support added for Identity Service, Object Storage Service
