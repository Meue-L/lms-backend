from account.repository.account_repository_impl import AccountRepositoryImpl
from account.repository.profile_repository_impl import ProfileRepositoryImpl
from account.service.account_service import AccountService

class AccountServiceImpl(AccountService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__profileRepository = ProfileRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def checkEmailDuplication(self, email):
        profile = self.__profileRepository.findByEmail(email)
        return profile is not None

    def registerAccount(self, Attendance_date, Attendance_cherry, Cherry, Ticket, paidmemberType, loginType, email, password, nickname):
        print("어카운트 서비스 접근")
        account = self.__accountRepository.create(Attendance_date, Attendance_cherry, Cherry, Ticket, paidmemberType, loginType)
        return self.__profileRepository.create(email, password, nickname, account)

    def registerSocialAccount(self, paidmemberType, loginType, email):
        account = self.__accountRepository.create(paidmemberType, loginType)
        return self.__profileRepository.createSocial(email, account)

    def decryptionPassword(self, email, password):
        return self.__profileRepository.decryption(email, password)

    def checkLoginType(self, email):
        loginType = self.__profileRepository.findByLoginType(email)
        return loginType

    def findAccountByEmail(self, email):
        profile = self.__profileRepository.findByEmail(email)
        return profile

    def findEmailByAccountId(self, accountId):
        email = self.__profileRepository.findByAccount(accountId)
        return email

    def findPaidMemberTypeByAccountId(self, accountId):
        paidmembertype = self.__accountRepository.findPaidMemberType(accountId)
        return paidmembertype

    def findTicketByAccountId(self, accountId):
        ticket = self.__accountRepository.findTicket(accountId)
        return ticket

    def checkNickNameDuplication(self, nickname):
        nickname = self.__profileRepository.findByNickname(nickname)
        return nickname is not None

    def updateTicketCount(self, user_id, new_ticket_count):
        ticket = self.__accountRepository.updateTicket(user_id, new_ticket_count)
        return ticket

    def findNicknameByAccountId(self, accountId):
        nickname = self.__profileRepository.findByNickname(accountId)
        return nickname

    def findCherryByAccountId(self, accountId):
        cherry = self.__accountRepository.findCherry(accountId)
        return cherry

    def findAttendance_CherryByAccountId(self, accountId):
        print("findAttendance_CherryByAccountId() 접근")
        attendance_cherry = self.__accountRepository.findAttendance_Cherry(accountId)
        return attendance_cherry

    def findAttendance_DateByAccountId(self, accountId):
        attendance_date = self.__accountRepository.findAttendance_Date(accountId)
        return attendance_date