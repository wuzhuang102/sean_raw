# 认证、授权与安全调研来源

recorded: 2026-06-10

本 raw 文件记录本次“认证、授权与安全”后端详细知识点页使用的稳定公开来源。正文知识页不翻译来源原文，只做后端工程视角的归纳。

## 主要来源

- OWASP Authentication Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
- OWASP Authorization Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html
- OWASP Session Management Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
- RFC 9700: Best Current Practice for OAuth 2.0 Security: https://www.rfc-editor.org/rfc/rfc9700.html
- OpenID Connect Core 1.0: https://openid.net/specs/openid-connect-core-1_0.html
- Apereo CAS Protocol: https://apereo.github.io/cas/development/protocol/CAS-Protocol.html
- NIST SP 800-63B: Authentication and Authenticator Management: https://pages.nist.gov/800-63-4/sp800-63b.html

## 链接验证

- 2026-06-10 使用 `curl -I` 验证 OWASP Authentication、Authorization、Session Management 页面返回 HTTP 200。
- 2026-06-10 使用 `curl -I` 验证 NIST SP 800-63B 页面返回 HTTP 200。
- 2026-06-10 使用浏览器检索验证 RFC 9700 HTML 页面可访问；`curl -I https://www.rfc-editor.org/rfc/rfc9700.html` 在当前环境返回 404，但页面正文可通过 web open 读取，因此知识页保留该稳定 RFC 链接。
- 2026-06-11 使用 `curl -I` 验证 Apereo CAS 主页、Apereo CAS Protocol 文档和 OpenID Connect Core 1.0 页面返回 HTTP 200。

## 本次取舍

- 覆盖后端日常高频知识：认证、会话、JWT、OAuth/OIDC、CAS 对比、权限模型、密码安全、API Key、服务间认证、常见 Web/API 漏洞、审计与密钥管理。
- 不展开偏冷门或过专门化内容：SAML 细节、Kerberos、硬件安全模块、复杂企业 IAM 产品配置、低层密码学算法推导、浏览器扩展安全、移动端专门威胁模型。
