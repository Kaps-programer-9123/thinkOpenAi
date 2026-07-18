---

# My understanding

I don't think **NexCore** should be marketed as

> AI chatbot for insurance.

Instead it should be

> **NexCore — An Agentic AI Platform for Enterprise Insurance Operations**

The user only sees a conversation.

Behind the scenes there are many agents, policies, workflows, memories and enterprise APIs.

---

# High Level Architecture

```text
                    Customer

                       │

         Voice / Web / Mobile / Teams

                       │
         (WebSocket / HTTP Streaming)

                       │

              NexCore Gateway
      (Authentication • Sessions • Routing)

                       │
     ─────────────────────────────────────

             Supervisor Agent

                       │
       Determines user's intent

                       │

 ┌──────────┬──────────┬──────────┬──────────┐
 │          │          │          │          │
 │ Policy   │ Quote    │ Claims   │ Renewal  │
 │ Agent    │ Agent    │ Agent    │ Agent    │
 │          │          │          │          │
 └──────────┴──────────┴──────────┴──────────┘

                │
                ▼

        Workflow / Decision Engine

                │

        Tool Calling Framework

─────────────────────────────────────────────

Enterprise APIs

Guidewire
CRM
Policy Admin
Billing
Payments
Document Store
Customer Profile
Knowledge Base
Vector Search
Web Search
Email
SMS

─────────────────────────────────────────────

Memory Layer

Conversation Memory
Customer Memory
Session Memory
Workflow State
Audit Logs
Preferences

─────────────────────────────────────────────

LLM Layer

Claude
GPT
Llama
Bedrock
Gemini

─────────────────────────────────────────────

Observability

Tracing
Metrics
Costs
Latency
Failures
Human Escalation
```

Notice something.

The LLM is almost at the bottom.

That's intentional.

The product is not GPT.

The product is the orchestration.

---

# Example

Customer says

> "I want to continue my policy but also change my address."

Supervisor thinks

```
Intent

↓

Policy Modification

↓

Needs Address Validation

↓

Needs Renewal Check

↓

Needs Premium Recalculation

↓

Needs Payment

↓

Done
```

The user only asked one sentence.

Behind the scenes maybe 12 operations happen.

---

# I think NexCore should think in Tasks

Not messages.

Every message becomes a task.

```
User

↓

Task

↓

Plan

↓

Execute

↓

Validate

↓

Complete

↓

Respond
```

That's much closer to how enterprise software works.

---

# Every Agent owns one capability

```text
Supervisor

│

├── Policy Agent

├── Quote Agent

├── Claims Agent

├── Renewal Agent

├── Customer Agent

├── Knowledge Agent

├── Search Agent

├── Notification Agent

├── Fraud Agent

├── Human Escalation Agent
```

Each agent knows one thing.

No huge prompts.

---

# Each agent owns tools

Policy Agent

```
get_policy()

renew_policy()

cancel_policy()

change_address()

update_vehicle()

change_nominee()
```

Claims Agent

```
create_claim()

upload_documents()

claim_status()

estimate_damage()
```

Knowledge Agent

```
RAG Search

Policy documents

FAQ

Compliance

Internal SOP
```

Search Agent

```
Google

Weather

DVLA

Government APIs

News

External regulations
```

---

# Memory isn't one database

Think of multiple memories.

```
Memory

│

├── Conversation

├── Customer

├── Workflow

├── Temporary

├── Long Term

├── Audit
```

Example

Customer

```
My car registration is AB12 XYZ
```

Conversation Memory

```
Current conversation
```

Customer Memory

```
Vehicle

Policy number

Address
```

Workflow Memory

```
Renewal started

Payment pending
```

---

# Workflow Engine

This is where enterprise systems become interesting.

Imagine

```
Renew Policy

↓

Policy exists?

↓

YES

↓

Payment received?

↓

NO

↓

Call Payment Agent

↓

Payment Success?

↓

YES

↓

Generate documents

↓

Send Email

↓

Complete
```

That is not GPT.

That is workflow.

---

# Decision Engine

Every enterprise has rules.

```
Premium > £5000

↓

Human Approval
```

```
Customer age < 18

↓

Reject
```

```
Vehicle modified

↓

Recalculate quote
```

```
Address changed

↓

Run fraud check
```

---

# Failure Handling

This is where most demos fail.

Example

```
Quote API Down

↓

Retry

↓

Retry

↓

Retry

↓

Fallback API

↓

Still fails

↓

Human Queue

↓

Notify Customer
```

An enterprise platform always plans for failures.

---

# Human Escalation

```
Customer Angry

↓

Sentiment Analysis

↓

Confidence Low

↓

Forward Call

↓

Human Agent

↓

Conversation History Shared
```

This is a key capability for contact centers.

---

# Voice

```
Customer Speaks

↓

Speech To Text

↓

Supervisor

↓

Agents

↓

Response

↓

Text To Speech

↓

Customer Hears
```

The agents never know if the user typed or spoke.

---

# Enterprise Tool Layer

Rather than hardcoding integrations, define tools behind interfaces.

```
Policy Tool

↓

Guidewire API

Billing Tool

↓

Billing API

Search Tool

↓

Google

Email Tool

↓

SMTP

SMS Tool

↓

Twilio

Storage Tool

↓

S3

Document Tool

↓

OCR
```

Agents only know they have a tool—they don't care how it's implemented.

---

# What excites me most

I would **not** build NexCore as an "insurance AI."

I would build it as a **generic enterprise agent platform**, with **insurance as the first implementation**.

So the core platform remains domain-agnostic:

```
                NexCore

          Agent Runtime

         Session Manager

        Workflow Engine

       Decision Engine

      Tool Orchestrator

      Memory Framework

      Prompt Library

     Human Escalation

       Observability

       Voice Support

      Multi-Agent Bus

         Gateway
```

Then plug in domain packages.

```
Insurance Package

Policy Agent

Claims Agent

Renewal Agent

Quote Agent

Guidewire Tools

Policy Admin APIs

-------------------------

Healthcare Package

Appointment Agent

Doctor Agent

EMR APIs

-------------------------

Banking Package

Account Agent

Payment Agent

Fraud Agent
```
