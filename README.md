# mod_kms_env

An Apache module that decrypts and sets environment variables using AWS Key Management Service (KMS).  Requires that you be running under an IAM role that has access to decrypt all of the encrypted variables or Apache won't start.

## Configuration options:

* KmsEnvRegion $region

Sets the region id you wish to use KMS in.  Defaults to the region that the instance is running in.

Example: KmsEnvRegion us-east-1

* KmsEnvSet $varName $payload

Sets the environment variable $varName to the result of running the KMS decrypt operation on $payload.

$payload is JSON-encoded and at least contains a CiphertextBlob field.

Example: KmsEnvSet test "{\"CiphertextBlob\":\"foo\"}"

* KmsEnvUnset $varName

Removes $varName from the environment for that context.  Useful if you want to disable a variable in a subdirectory or something.
