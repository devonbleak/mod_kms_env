# mod_kms_env

An Apache module that decrypts and sets environment variables using AWS Key Management Service (KMS).  Requires that you be running under an IAM role that has access to decrypt all of the encrypted variables or Apache won't start.

## Configuration

    LoadModule kms_env_module modules/mod_kms_env.so

`KmsEnvRegion` will change the AWS region that the module contacts KMS in.

    KmsEnvRegion us-east-1

`KmsEnvSet <varName> <payload>` will set environment variable `varName` to the result of decrypting `payload`.  `payload` is a json-formatted string and at a minimum needs to include a `CiphertextBlob` field as well as the encryption context that was used to encrypt the original data, if any.

    KmsEnvSet test '{"CiphertextBlob":"..."}'

`KmsEnvUnset <varName>` will unset the environment variable `varName` if it was previously set by this module.  Note that unsetting variables using mod_env's UnsetEnv will have no effect.

    KmsEnvUnset test
