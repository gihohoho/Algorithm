-- 코드를 입력하세요
# 중성화 : Neutered Male, Spayed Female
SELECT o.ANIMAL_ID, o.ANIMAL_TYPE, o.NAME from ANIMAL_INS i
inner join ANIMAL_OUTS o on i.ANIMAL_ID = o.ANIMAL_ID
where i.SEX_UPON_INTAKE != o.SEX_UPON_OUTCOME