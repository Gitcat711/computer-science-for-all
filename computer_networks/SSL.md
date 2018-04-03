# Importance of SSL.
> SSL is most commonly used transport layer security protocol. Depending on how SSL is implemented and configured, it can provide any combination of the following types of protection:

- **Confidentiality:** SSL can ensure that data cannot be read by unauthorised parties. This is accomplished by encrypting data using a cryptographic algorithm and a secret key - _a value known to two parties exchanging data._ The data can only be decrypted by someone who has he secret key.

- **Integrity:** SSL can determine if data has been changed(_intentionally or unintentionally_) during transit. The integrity of data can be assured by generating a message authentication code(MAC) value, which is keyed cryptographic checksum of the data. If the data is altered and the MAC is recalculated, the old and new MACs will differ.

- **Peer Authentication:** Each SSL endpoint can confirm the identity of the other SSL endpoint with which it wishes to communicate, ensuring that the network traffic and data is being sent from the expected host. SSL authentication is typically performed one-way, authenticating the server to the client, but it can be performed mutually.

- **Replay Protection:** The same data is not delivered multiple times, and data is not delivered grossly out of order.
