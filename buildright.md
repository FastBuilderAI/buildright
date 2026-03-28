# BuildRight: Universal Coding Health Layer

## Twelve Factor App

### [ID: FACTOR_1_CODEBASE]
**Action:** Maintain_One_Repo
**Input:** {Context}
**Logic:** Use one codebase tracked in revision control; many deploys. Each app should reside in a single repository and never share code with other apps (use libraries instead).
**Data_Connections:** [git_repository], [version_control], [codebase_integrity]
**Access:** Role_Developer
**Events:** On_Project_Initialization

### [ID: FACTOR_2_DEPENDENCIES]
**Action:** Explicit_Expose_Deps
**Input:** {Context}
**Logic:** Explicitly declare and isolate dependencies. Never rely on the implicit existence of system-wide packages. Use dependency managers (e.g., pip, npm, gems).
**Data_Connections:** [dependency_manifest], [manifest_file], [isolation_layer]
**Access:** Role_DevOps_Engineer
**Events:** On_Build

### [ID: FACTOR_3_CONFIG]
**Action:** Store_Env_Vars
**Input:** {Context}
**Logic:** Store configuration in the environment. Separate config and code; use environment variables for resource handles and credentials.
**Data_Connections:** [environment_variables], [secrets_manager], [dynamic_config]
**Access:** Role_System_Admin
**Events:** On_Runtime_Init

### [ID: FACTOR_4_BACKING_SERVICES]
**Action:** Treat_As_Resources
**Input:** {Context}
**Logic:** Treat backing services as attached resources. Any service should be swappable by changing the resource handle (e.g., DB switch from local to RDS).
**Data_Connections:** [resource_handles], [swappable_services], [connection_strings]
**Access:** Role_Architect
**Events:** On_Infrastructure_Provisioning

### [ID: FACTOR_5_BUILD_RELEASE_RUN]
**Action:** Separate_Stages
**Input:** {Context}
**Logic:** Strictly separate build, release, and run stages. Build turns code into an executable bundle; release combines bundle with config; run executes the release.
**Data_Connections:** [ci_cd_stages], [immutable_releases], [artifact_storage]
**Access:** Role_DevOps_Engineer
**Events:** On_Pipeline_Execution

### [ID: FACTOR_6_PROCESSES]
**Action:** Execute_Stateless
**Input:** {Context}
**Logic:** Execute the app as one or more stateless processes. Share nothing; store persistent data in a stateful backing service (e.g., Redis, DB).
**Data_Connections:** [stateless_logic], [session_externalization], [transient_storage]
**Access:** Role_Architect
**Events:** On_Process_Design

### [ID: FACTOR_7_PORT_BINDING]
**Action:** Export_Services_via_Port
**Input:** {Context}
**Logic:** Export services via port binding. The app is completely self-contained; do not rely on runtime injection of webservers (e.g., use an internal webserver).
**Data_Connections:** [self_contained_app], [port_allocation], [http_listening]
**Access:** Role_Network_Engineer
**Events:** On_Service_Startup

### [ID: FACTOR_8_CONCURRENCY]
**Action:** Scale_Via_Process
**Input:** {Context}
**Logic:** Scale out via the process model. Each process type should be independently scaleable; use workers for background tasks.
**Data_Connections:** [process_replication], [horizontal_scaling], [load_balancing]
**Access:** Role_SRE_Engineer
**Events:** On_Scaling_Event

### [ID: FACTOR_9_DISPOSABILITY]
**Action:** Maximize_Robustness
**Input:** {Context}
**Logic:** Maximize robustness with fast startup and graceful shutdown. Processes should start in seconds and shut down cleanly when receiving signals (SIGTERM).
**Data_Connections:** [graceful_shutdown], [fast_startup], [signal_handling]
**Access:** Role_DevOps_Engineer
**Events:** On_Process_Termination

### [ID: FACTOR_10_DEV_PROD_PARITY]
**Action:** Minimize_Gap
**Input:** {Context}
**Logic:** Keep development, staging, and production as similar as possible. Use the same backing services and minimize gaps between environments.
**Data_Connections:** [environment_parity], [infrastructure_as_code], [identical_stacks]
**Access:** Role_QA_Engineer
**Events:** On_Environment_Setup

### [ID: FACTOR_11_LOGS]
**Action:** Treat_As_Streams
**Input:** {Context}
**Logic:** Treat logs as event streams. Do not write to local files; write to stdout for external aggregation (e.g., ELK, Splunk).
**Data_Connections:** [log_streaming], [stdout_logging], [event_aggregation]
**Access:** Role_Observability_Engineer
**Events:** On_Runtime_Logging

### [ID: FACTOR_12_ADMIN_PROCESSES]
**Action:** Run_One_Off_Tasks
**Input:** {Context}
**Logic:** Run admin/management tasks as one-off processes. Run scripts inside the release environment (e.g., database migrations).
**Data_Connections:** [migration_scripts], [one_off_execution], [admin_tools]
**Access:** Role_DB_Admin
**Events:** On_Maintenance

## Clean Code SOLID

### [ID: SOLID_SRP]
**Action:** Enforce_SRP
**Input:** {Context}
**Logic:** Single Responsibility Principle: A class should have one reason to change. Decouple logic into specialized components.
**Data_Connections:** [module_decoupling], [focused_classes], [single_responsibility]
**Access:** Role_Architect
**Events:** On_Design

### [ID: SOLID_OCP]
**Action:** Enforce_OCP
**Input:** {Context}
**Logic:** Open-Closed Principle: Open for extension, closed for modification. Use interfaces and abstraction layers.
**Data_Connections:** [polymorphism], [interfaces], [extensions]
**Access:** Role_Architect
**Events:** On_Expansion

### [ID: SOLID_LSP]
**Action:** Enforce_LSP
**Input:** {Context}
**Logic:** Liskov Substitution Principle: Objects of a superclass should be replaceable with objects of its subclasses without breaking the application.
**Data_Connections:** [inheritance_integrity], [interface_compliance], [contract_trust]
**Access:** Role_Architect
**Events:** On_Subclass_Creation

### [ID: SOLID_ISP]
**Action:** Enforce_ISP
**Input:** {Context}
**Logic:** Interface Segregation Principle: No client should be forced to depend on methods it does not use. Clients should not be forced to implement interfaces they don't use.
**Data_Connections:** [fine_grained_interfaces], [client_focus], [no_fat_interfaces]
**Access:** Role_Architect
**Events:** On_API_Definition

### [ID: SOLID_DIP]
**Action:** Enforce_DIP
**Input:** {Context}
**Logic:** Dependency Inversion Principle: Depend on abstractions, not concretions. Use dependency injection repositories.
**Data_Connections:** [abstractions], [dependency_injection], [inversion_control]
**Access:** Role_Architect
**Events:** On_Service_Init

### [ID: CLEAN_DRY]
**Action:** Avoid_Repetition
**Input:** {Context}
**Logic:** Don't Repeat Yourself: Eliminate code duplication. Consolidation of logic ensures a single source of truth.
**Data_Connections:** [code_reuse], [abstraction], [authority_source]
**Access:** Role_Developer
**Events:** On_Review

### [ID: CLEAN_KISS]
**Action:** Simplify_Complexity
**Input:** {Context}
**Logic:** Keep It Simple, Stupid: Avoid over-engineering. Simplicity is the ultimate sophistication in software engineering.
**Data_Connections:** [simplicity], [minimalism], [logic_purity]
**Access:** Role_Developer
**Events:** On_Review

### [ID: CLEAN_YAGNI]
**Action:** Defer_Over_Engineering
**Input:** {Context}
**Logic:** You Ain't Gonna Need It: Implement features only when needed, not when you foresee needing them. Focus on current requirements.
**Data_Connections:** [deferred_logic], [actual_needs], [minimal_set]
**Access:** Role_Developer
**Events:** On_Planning

### [ID: CLEAN_BOY_SCOUT]
**Action:** Leave_Better_Code
**Input:** {Context}
**Logic:** Leave the code cleaner than you found it. Refactor continuously as you work on features to prevent technical debt accumulation.
**Data_Connections:** [refactoring], [debt_reduction], [constant_improvement]
**Access:** Role_Developer
**Events:** On_Modification

### [ID: CLEAN_MEANINGFUL_NAMES]
**Action:** Use_Self_Documenting_Names
**Input:** {Context}
**Logic:** Names should be descriptive and unambiguous. Avoid short, cryptic labels; prefer readable, intent-revealing names.
**Data_Connections:** [descriptive_naming], [intent_logic], [readability]
**Access:** Role_Developer
**Events:** On_Variable_Init

## OWASP Top 10 2021

### [ID: OWASP_A01_BROKEN_ACCESS_CONTROL]
**Action:** Enforce_Least_Privilege
**Input:** {Context}
**Logic:** The principle of least privilege should be implemented throughout the application. Deny by default and only allow access based on explicit roles and context.
**Data_Connections:** [authorization_check], [multi_tenant_isolation], [role_metadata]
**Access:** Role_Security_Officer
**Events:** On_Resource_Access

### [ID: OWASP_A02_CRYPTOGRAPHIC_FAILURES]
**Action:** Protect_Sensitive_Data
**Input:** {Context}
**Logic:** Apply cryptographic controls to data at rest and in transit. Use strong algorithms (e.g., AES-256-GCM, SHA-256) and ensure proper key management.
**Data_Connections:** [encryption_at_rest], [tls_1.3], [key_management]
**Access:** Role_Cryptographer
**Events:** On_Data_Processing

### [ID: OWASP_A03_INJECTION]
**Action:** Sanitize_Input
**Input:** {Context}
**Logic:** Use parameterized queries and strongly typed APIs to prevent Injection attacks. Sanitize and validate all user-supplied input before use in sensitive operations.
**Data_Connections:** [parameterized_queries], [input_validation], [orm_safe_calls]
**Access:** Role_Security_Auditor
**Events:** On_External_Input

### [ID: OWASP_A04_INSECURE_DESIGN]
**Action:** Secure_By_Design
**Input:** {Context}
**Logic:** Use threat modeling, secure design patterns, and reference architectures to build a secure foundational structure.
**Data_Connections:** [threat_model], [secure_patterns], [security_boundary]
**Access:** Role_Architect
**Events:** On_Architectural_Decision

### [ID: OWASP_A05_SECURITY_MISCONFIG]
**Action:** Harden_Infrastructure
**Input:** {Context}
**Logic:** Ensure all software stacks are properly configured—remove default passwords, disable unnecessary services, and maintain secure environment settings.
**Data_Connections:** [hardening_config], [no_default_creds], [least_minimal_stack]
**Access:** Role_System_Admin
**Events:** On_Deployment

### [ID: OWASP_A06_VULNERABLE_COMPONENTS]
**Action:** Update_Dependencies
**Input:** {Context}
**Logic:** Continuously scan for and update outdated or vulnerable third-party components (SCA) and libraries to reduce attack surface.
**Data_Connections:** [dependency_scan], [patch_management], [bill_of_materials]
**Access:** Role_QA_Engineer
**Events:** On_Build

### [ID: OWASP_A07_IDENTIFICATION_FAILURES]
**Action:** Secure_Authentication
**Input:** {Context}
**Logic:** Implement robust multi-factor authentication (MFA) and secure identity management to protect user accounts from credential stuffing.
**Data_Connections:** [mfa_enforced], [session_security], [identity_provider]
**Access:** Role_Auth_Manager
**Events:** On_User_Session_Creation

### [ID: OWASP_A08_INTEGRITY_FAILURES]
**Action:** Verify_Data_Integrity
**Input:** {Context}
**Logic:** Verify the integrity of software updates, critical data, and CI/CD pipelines through digital signatures and non-repudiation mechanisms.
**Data_Connections:** [digital_signatures], [hash_verification], [pipeline_integrity]
**Access:** Role_DevOps_Engineer
**Events:** On_Deployment_Trigger

### [ID: OWASP_A09_LOGGING_FAILURES]
**Action:** Monitor_And_Alert
**Input:** {Context}
**Logic:** Log all critical security events, such as failed authentication attempts and access control failures. Implement real-time alerting to enable rapid incident response.
**Data_Connections:** [audit_logs], [siem_integration], [incident_alerts]
**Access:** Role_SOC_Analyst
**Events:** On_Security_Event

### [ID: OWASP_A10_SSRF]
**Action:** Restrict_Remote_Req
**Input:** {Context}
**Logic:** Prevent Screen-Side Request Forgery by implementing allow-lists for network domains and validating all URLs provided by clients.
**Data_Connections:** [url_allowlist], [network_segregation], [outbound_filtering]
**Access:** Role_Network_Engineer
**Events:** On_Remote_Request

## CWE Top 25 Key

### [ID: CWE_78_OS_COMMAND_INJECTION]
**Action:** Avoid_Shell_Commands
**Input:** {Context}
**Logic:** The software constructs all or part of an OS command using externally-influenced input, but it does not neutralize or incorrectly neutralizes special elements.
**Data_Connections:** [parameterized_os_calls], [no_shell_true], [input_sanitization]
**Access:** Role_Security_Auditor
**Events:** On_OS_Command

### [ID: CWE_79_XSS]
**Action:** Output_Encoding
**Input:** {Context}
**Logic:** The software does not neutralize or incorrectly neutralizes user-controllable input before it is placed in output that is used as a web page that is served to other users.
**Data_Connections:** [html_encoding], [content_security_policy], [js_escaping]
**Access:** Role_Security_Officer
**Events:** On_Web_Render

### [ID: CWE_89_SQL_INJECTION]
**Action:** Use_Prepared_Statements
**Input:** {Context}
**Logic:** The software constructs all or part of an SQL command using externally-influenced input, but it does not neutralize or incorrectly neutralizes special elements.
**Data_Connections:** [parameterized_queries], [prepared_statements], [orm_security]
**Access:** Role_DB_Security
**Events:** On_Database_Call

### [ID: CWE_125_OUT_OF_BOUNDS_READ]
**Action:** Check_Index_Bounds
**Input:** {Context}
**Logic:** The software reads data past the end, or before the beginning, of the intended buffer. This can allow attackers to read sensitive information or cause a crash.
**Data_Connections:** [bounds_check], [safe_iterators], [buffer_management]
**Access:** Role_C_Developer
**Events:** On_Memory_Access

### [ID: CWE_190_INTEGER_OVERFLOW]
**Action:** Use_Safe_Arithmetic
**Input:** {Context}
**Logic:** The software performs a calculation that can produce an integer overflow or wraparound, when the logic expects a smaller value.
**Data_Connections:** [unsigned_safeguards], [range_checks], [overflow_logic]
**Access:** Role_Security_Auditor
**Events:** On_Math_Operation

### [ID: CWE_200_INFO_EXPOSURE]
**Action:** Mask_Sensitive_Info
**Input:** {Context}
**Logic:** Avoid intentional or unintentional exposure of sensitive information to an unauthorized actor via error messages or logs.
**Data_Connections:** [no_stack_trace_in_prod], [masked_logs], [generic_error_msgs]
**Access:** Role_Security_Officer
**Events:** On_Error_Response

### [ID: CWE_287_IMPROPER_AUTH]
**Action:** Enforce_Strong_Auth
**Input:** {Context}
**Logic:** The software does not perform or incorrectly performs an authentication check when an actor attempts to access a resource.
**Data_Connections:** [multi_factor_auth], [session_integrity], [secure_identity]
**Access:** Role_Auth_Manager
**Events:** On_Auth_Challenge

### [ID: CWE_416_USE_AFTER_FREE]
**Action:** Manage_Memory_Lifecycle
**Input:** {Context}
**Logic:** Referencing memory after it has been freed can lead to arbitrary code execution or a crash. Ensure pointers are nullified after free.
**Data_Connections:** [nullify_pointers], [smart_pointers], [raii]
**Access:** Role_Lower_Level_Dev
**Events:** On_Memory_Free

### [ID: CWE_502_DESERIALIZATION]
**Action:** Restrict_Untrusted_Data
**Input:** {Context}
**Logic:** The application deserializes untrusted data without sufficiently verifying that the resulting data will be valid.
**Data_Connections:** [safe_deserializers], [no_pickle_untrusted], [signature_checks]
**Access:** Role_Security_Auditor
**Events:** On_Data_Ingest

### [ID: CWE_862_MISSING_AUTH]
**Action:** Deny_By_Default
**Input:** {Context}
**Logic:** The software does not perform an authorization check when an actor attempts to access a resource or perform an action.
**Data_Connections:** [access_control_matrix], [authorization_check], [policy_engine]
**Access:** Role_Security_Officer
**Events:** On_Action_Invocation

## Enterprise Standards

### [ID: ENT_01_LOGGING]
**Action:** Enforce_Structured_Logging
**Input:** {Context}
**Logic:** All application logs must be in JSON format and include trace_id, span_id, and service_name for distributed tracing.
**Data_Connections:** [json_logs], [trace_id], [distributed_tracing]
**Access:** Role_Observability_Engineer
**Events:** On_Log_Event

### [ID: ENT_02_HEALTH_CHECK]
**Action:** Implement_Liveness_Probes
**Input:** {Context}
**Logic:** Every microservice must expose a /health liveness probe and a /ready readiness probe for orchestrator integration.
**Data_Connections:** [liveness_probe], [readiness_probe], [k8s_health]
**Access:** Role_DevOps_Engineer
**Events:** On_Service_Deployment

