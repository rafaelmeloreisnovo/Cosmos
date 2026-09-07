# RafNet → Cosmos canon capability v1

State: `SOURCE_IMPLEMENTED / PROVIDER_AND_CROSS_REPO_EXECUTION_PENDING`  
Capability: `cosmos.canon.validate`  
Consumer base: `Cosmos@de1c5a88913f5d6ee6e90b7b09750923c91cb4df`  
`claim_allowed=false`

## Why this capability exists

Cosmos already contains an exact canon validator whose source explicitly limits itself to `[E]` exact/combinatorial invariants and refuses to promote conventions, hypotheses or parables to physical claims.

The RafNet integration exposes only that bounded operation. It does not expose the general shell, the full-stack API, arbitrary claim scoring, deployment, database writes, or research publication actions.

## Contract

Machine-readable contract:

`contracts/rafnet/cosmos.canon.validate.v1.json`

Adapter:

`scripts/federation/rafnet_canon_validate_v1.py`

Bound existing executor:

`scripts/formal/validate-cosmos-canon.py`

Expected Git blob SHA-1:

`be1713d517af16dbc9ca204fa2c0e6a71e054314`

Contract drift is fail-closed.

## Payload

The only accepted payload is the literal:

```text
CANON_EXACT_V1
```

Maximum size is 64 bytes. Arbitrary commands and private embedded data are not accepted.

## Required RafNet context

The adapter requires:

```text
RAFNET_TARGET_CAPABILITY=cosmos.canon.validate
RAFNET_MESSAGE_ID=<non-empty message id>
RAFNET_SOURCE_COMMIT=<40 lowercase hex commit>
```

This context binds the local result to the transport message. It does not prove network peer identity by itself.

## Result boundary

A successful adapter result means only:

```text
existing exact canon validator executed
+ its declared exact/combinatorial invariants returned PASS
```

It explicitly returns:

```text
hypotheses_validated=false
physical_claims_proven=false
scientific_generalization_allowed=false
claim_allowed=false
```

Therefore:

```text
canon PASS != cosmological theory proven
canon PASS != physical law established
canon PASS != peer review
canon PASS != publication readiness
canon PASS != patentability
```

## Tests

`tests/test_rafnet_canon_capability_v1.py` checks:

- exact binding to the existing validator;
- execution of the existing exact canon validator;
- wrong payload rejection;
- wrong capability rejection;
- missing message-id rejection;
- malformed source-commit rejection;
- result JSON serialization;
- mandatory non-promotion of scientific/physical claims.

## R3

- **F_ok:** bounded source-backed capability is materialized without expanding Cosmos authority.
- **F_gap:** current-head CI, RafNet dispatch binding, exact cross-repository fixture and physical Termux execution are not yet proven.
- **F_next:** bind this exact capability into the RafNet authority registry and dispatcher; then run a synthetic cross-repo receipt chain.
