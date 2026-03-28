# BuildRight: Universal Coding Health Layer

## Security OWASP

### [ID: OWASP_A1_INJECTION]
**Action:** Prevent_Injection
**Input:** {Context}
**Logic:** Always use parameterized queries or prepared statements for database, LDAP, and OS command calls. Never concatenate unsanitized user input into executable strings.
**Data_Connections:** [parameterized_queries], [sql_injection], [prepared_statements]
**Access:** Role_Security_Auditor
**Events:** On_Database_Query

### [ID: OWASP_A2_BROKEN_AUTH]
**Action:** Secure_Authentication
**Input:** {Context}
**Logic:** Implement secure session management, multi-factor authentication, and robust password hashing (e.g., Argon2, bcrypt). Protect against session hijacking and automated credential stuffing.
**Data_Connections:** [session_token], [mfa], [password_hashing]
**Access:** Role_Auth_Manager
**Events:** On_User_Login

### [ID: OWASP_A3_SENSITIVE_DATA]
**Action:** Protect_Data
**Input:** {Context}
**Logic:** Encrypt sensitive data at rest using AES-256 and in transit using TLS 1.3. Avoid storing unnecessary PII and rotate encryption keys periodically.
**Data_Connections:** [encryption_at_rest], [tls_1.3], [pii]
**Access:** Role_Compliance_Officer
**Events:** On_Data_Storage

## Architecture SOLID

### [ID: SOLID_SRP]
**Action:** Enforce_SRP
**Input:** {Context}
**Logic:** Single Responsibility Principle: A class or module should have one, and only one, reason to change. Decouple logic into specialized, focused components.
**Data_Connections:** [module_decoupling], [focused_classes], [single_responsibility]
**Access:** Role_Architect
**Events:** On_Component_Design

### [ID: SOLID_OCP]
**Action:** Enforce_OCP
**Input:** {Context}
**Logic:** Open-Closed Principle: Software entities should be open for extension but closed for modification. Use interfaces and polymorphism to allow behavior changes without altering existing code.
**Data_Connections:** [polymorphism], [interfaces], [extensions]
**Access:** Role_Architect
**Events:** On_Feature_Expansion

### [ID: SOLID_DIP]
**Action:** Enforce_DIP
**Input:** {Context}
**Logic:** Dependency Inversion Principle: High-level modules should not depend on low-level modules. Both should depend on abstractions. Use dependency injection to manage lifecycle and mockability.
**Data_Connections:** [dependency_injection], [abstractions], [mocking]
**Access:** Role_Architect
**Events:** On_Service_Initialization

## Code Hygiene

### [ID: PRINCIPLE_DRY]
**Action:** Avoid_Repetition
**Input:** {Context}
**Logic:** Don't Repeat Yourself: Every piece of knowledge must have a single, unambiguous, authoritative representation within a system. Use abstractions to consolidate duplicated logic.
**Data_Connections:** [code_reuse], [abstraction_layer], [authority_source]
**Access:** Role_Developer
**Events:** On_Code_Review

### [ID: PRINCIPLE_KISS]
**Action:** Simplify_Logic
**Input:** {Context}
**Logic:** Keep It Simple, Stupid: Most systems work best if they are kept simple rather than made complicated; therefore, simplicity should be a key goal in design, and unnecessary complexity should be avoided.
**Data_Connections:** [simplicity], [minimalism], [no_overengineering]
**Access:** Role_Developer
**Events:** On_Logic_Implementation

### [ID: PRINCIPLE_YAGNI]
**Action:** Defer_Features
**Input:** {Context}
**Logic:** You Ain't Gonna Need It: Always implement things when you actually need them, never when you just foresee that you may need them. Avoid speculative generality.
**Data_Connections:** [deferred_execution], [actual_requirements], [no_speculation]
**Access:** Role_Developer
**Events:** On_Project_Planning

## Clean Code

### [ID: CLEAN_NAMES]
**Action:** Use_Meaningful_Names
**Input:** {Context}
**Logic:** Variables, functions, and classes should have names that reveal intent. A name should tell you why it exists, what it does, and how it is used.
**Data_Connections:** [intent_naming], [self_documenting], [readability]
**Access:** Role_Developer
**Events:** On_Variable_Declaration

### [ID: CLEAN_FUNCTIONS]
**Action:** Keep_Functions_Small
**Input:** {Context}
**Logic:** Functions should be small, should do only one thing, and should do it well. Large functions indicate high cyclomatic complexity and low maintainability.
**Data_Connections:** [functional_purity], [cyclomatic_complexity], [small_scope]
**Access:** Role_Developer
**Events:** On_Function_Definition

